from collections import Counter

def calc_bigram_value(bigram1, bigram2):
    direction_diff = abs(bigram1["direction"] - bigram2["direction"])
    # 0 deg and 360 deg are the same point on a circle
    direction_diff = min(direction_diff, 360 - direction_diff)
    # 1 is completely ambiguous; 0 unambiguous
    direction_value = max((-1.0/90.0) * direction_diff + 1, 0)

    magnitude_diff = abs(bigram1["magnitude"] - bigram2["magnitude"])
    magnitude_value = max((-1.0/3.0) * magnitude_diff + 1, 0)

    bigram_value = direction_value * magnitude_value

    return bigram_value

def calc_pair_value(word1, word2):
    pair_value = 1
    for bigram_num, bigram in enumerate(word1):
        bigram_value = calc_bigram_value(bigram, word2[bigram_num])
        # if one bigram is unambiguous, rest of word is too
        if bigram_value == 0:
            return 0
        else:
            pair_value *= bigram_value
    return pair_value

def calc_layout_results(layout_paths):
    match_paths = layout_paths.copy()

    # set default dict value to integer
    layout_results = Counter()

    for word, word_bigrams in layout_paths.iteritems():
        for match, match_bigrams in match_paths.iteritems():
            if len(word_bigrams) == len(match_bigrams) and word != match:
                pair_value = calc_pair_value(word_bigrams, match_bigrams)
                pair_value = round(pair_value,2)
                layout_results[pair_value] += 1

        # once something has been compared with everything remove it
        match_paths.pop(word, None)

    return layout_results