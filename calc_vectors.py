import math

# calculate vector paths for words
def split_bigrams(word):
    word_bigrams = []
    for letter_pos in range(len(word) - 1):
        bigram = [word[letter_pos], word[letter_pos + 1]]
        word_bigrams.append(bigram)
    return word_bigrams

def calc_word_vector(word, layout):
    word = word.lower()
    # one char words don't have vectors
    if len(word) > 1:
        word_bigrams = split_bigrams(word)
        steps = []

        for bigram_num, bigram in enumerate(word_bigrams):

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

            steps.append(step)
                
        # if two consecutive bigrams share direction, combine attributes
        # combine into previous step may give efficiency gains
        for step_num, step in enumerate(steps):
            if step_num + 1 < len(steps):
                next_step = steps[step_num + 1]

                if (step['direction'] == next_step['direction'] or
                                         next_step['magnitude'] == 0):
                    step['dx'] += next_step['dx']
                    step['dy'] += next_step['dy']
                    step['magnitude'] += next_step['magnitude']
                    # the second bigram path is now incorporated in
                    # the first's path, remove it
                    steps.pop(step_num + 1)

        return steps
    else:
        return []
