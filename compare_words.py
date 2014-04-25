import pickle

# get word paths
with open("word_path_defs.pickle", "rb") as handle:
    paths = pickle.load(handle)

# compare vectors for similarity
def path_match(word1, word2):
    for bigram_num, bigram in enumerate(word1):
        match_bigram = word2[bigram_num]

        direction_diff = bigram['direction'] - match_bigram['direction']
        dir_bounds = 10
        within_direction_bounds = (-dir_bounds < direction_diff < dir_bounds or
                                    direction_diff > 360 - dir_bounds or 
                                    direction_diff < -360 + dir_bounds)

        magnitude_diff = bigram['magnitude'] - match_bigram['magnitude']
        mag_bounds = 1.5
        within_magnitude_bounds = -mag_bounds < magnitude_diff < mag_bounds

        if not within_direction_bounds or not within_magnitude_bounds:
            return False
    else:
        return True

for layout_name, layout in paths.iteritems():

    match_layout = layout.copy()
    print "on the %s layout" % (layout_name)

    for word in layout:
        for match in match_layout:
            if len(layout[word]) == len(match_layout[match]) and word != match:
                if path_match(layout[word], match_layout[match]):
                    print "  ", word, match
                    # print "    word[0]:", layout[word][0]
                    # print "    match[0]:", layout[match][0]

        # once something has been compared with everything remove it
        match_layout.pop(word, None)

    print "=============="