import pickle
from collections import defaultdict

# get word vector paths
with open("word_path_defs.pickle", "rb") as handle:
    paths = pickle.load(handle)

def calc_bigram_value(bigram1, bigram2):

    direction_diff = abs(bigram1["direction"] - bigram2["direction"])
    direction_diff = min(direction_diff, 360 - direction_diff)

    # 1 is completely ambiguous; 0 unambiguous
    direction_value = max((-1.0/90.0) * direction_diff + 1, 0)

    magnitude_diff = abs(bigram1["magnitude"] - bigram2["magnitude"])
    magnitude_value = max((-1.0/3.0) * magnitude_diff + 1, 0)

    bigram_value = direction_value * magnitude_value

    # print "  ", bigram1, bigram2
    # print "  dir_dif:", direction_diff
    # print "  dir_val:", direction_value
    # print "  mag_dif:", magnitude_diff
    # print "  mag_val:", magnitude_value
    # print "  big_val:", bigram_value

    return bigram_value

def calc_pair_value(word1, word2):

    pair_value = 1
    for bigram_num, bigram in enumerate(word1):
        bigram_value = calc_bigram_value(bigram, word2[bigram_num])
        # if one bigram is unambiguous, rest of pair is too
        if bigram_value == 0:
            return 0
        else:
            pair_value *= bigram_value
    return pair_value

for layout_name, layout in paths.iteritems():
    match_layout = layout.copy()
    # layout_results = {
    #     0:0,
    #     1:0
    #     }

    layout_results = defaultdict(int)

    print "============================"
    print "on the %s layout" % layout_name

    for word, word_bigrams in layout.iteritems():
        for match, match_bigrams in match_layout.iteritems():
            if len(word_bigrams) == len(match_bigrams) and word != match:
                pair_value = calc_pair_value(word_bigrams, match_bigrams)
                pair_value = round(pair_value,2)
                layout_results[pair_value] += 1

                PAIR_THRESHOLD = 0.8
                if pair_value >= PAIR_THRESHOLD:
                    print pair_value, ":", word, match
        # once something has been compared with everything remove it
        match_layout.pop(word, None)

    # print "on the %s layout" % layout_name
    print "=============="
    for pair_value in sorted(layout_results):
        print "  %s: %s" % (pair_value, layout_results[pair_value])