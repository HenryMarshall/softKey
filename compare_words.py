import pickle

# get word paths
with open("word_path_defs.pickle", "rb") as handle:
    paths = pickle.load(handle)

def path_match(word1, word2):
    for bigram_num, bigram in enumerate(word1):
        match_bigram = word2[bigram_num]

        direction = bigram['direction'] != match_bigram['direction']
        magnitude_diff = bigram['magnitude'] - match_bigram['magnitude']
        if direction or magnitude_diff < -2 or magnitude_diff > 2:
            return False
            # print "bigram %s matches direction" % bigram_num
            # print "word bigram:", bigram
            # print "match bigram:", match_bigram
    else:
        return True

for layout_name, layout in paths.iteritems():

    match_layout = layout.copy()
    print "on the %s layout" % (layout_name)

    for word in layout:
        for match in match_layout:
            if len(layout[word]) == len(match_layout[match]) and word != match:
                if path_match(layout[word], match_layout[match]):
                    print word, match

        # once something has been compared with everything remove it
        match_layout.pop(word, None)

    print "=============="