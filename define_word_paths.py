#!/usr/bin/python

import pickle
import math
import sys


##### TO DO #####
# accept corpus in non-list format
# remove duplicate words from corpus
# error handling for capitals, non-included chars


# load character positions
with open('character_positions.pickle', 'rb') as handle:
    character_positions = pickle.load(handle)


# load corpus

f = open(sys.argv[1])
corpus = f.read().split('\n')


# generate results

# creates list of bigrams in word
def split_bigrams(word):
    word_bigrams = []
    for letter_pos in range(len(word) - 1):
        bigram = [word[letter_pos], word[letter_pos + 1]]
        word_bigrams.append(bigram)
    return word_bigrams

results = {}

for layout_name, layout in character_positions.iteritems():
    
    results[layout_name] = {}

    for word in corpus:
        word = word.lower()

        # one character words don't have bigrams
        if len(word) > 1:

            word_bigrams = split_bigrams(word)
            results[layout_name][word] = []

            for bigram in word_bigrams:

                # calculate vector for bigram
                step = {
                    'dx': layout[bigram[1]]['x'] - layout[bigram[0]]['x'],
                    'dy': layout[bigram[1]]['y'] - layout[bigram[0]]['y'],
                }

                direction = math.degrees(math.atan2(step['dy'], step['dx']))
                # atan2 returns values from +1 to -1 rad
                if direction < 0:
                    direction = 360 + direction

                step.update({
                    'direction': direction,
                    'magnitude': (step['dx'] ** 2 + step['dy'] ** 2) ** 0.5
                })
                results[layout_name][word].append(step)


with open('word_path_defs.pickle', 'wb') as handle:
    pickle.dump(results, handle)
