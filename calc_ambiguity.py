import argparse
import pickle

import calc_vectors
import calc_scores

# establish corpus from cli
parser = argparse.ArgumentParser(description="""Calculate the ambiguity of
    word pairings. Accepts words, and files prefixed with '@' (e.g., 
    @corpus.txt) with \\n delimited words.""",
    fromfile_prefix_chars='@')

parser.add_argument('words', metavar='N', type=str, nargs='+',
                    help='enter a series of words')
corpus = parser.parse_args()

# establish layouts
# with open('character_positions.pickle', 'rb') as handle:
with open('layouts/random_layouts_computer.pickle', 'rb') as handle:
    layouts = pickle.load(handle)

# calculate the vector path for each word on each layout
paths = {}
for layout_name, layout in layouts.iteritems():
    paths[layout_name] = {}

    for word in corpus.words:
        word_vector = calc_vectors.calc_word_vector(word, layout)
        paths[layout_name][word] = word_vector

# calculate the ambiguity of the corpus on each layout
layout_results = {}
for layout_name, layout_paths in paths.iteritems():
    ambiguity_results = calc_scores.calc_layout_results(layout_paths)
    layout_results[layout_name] = ambiguity_results


# write the results to a csv file
ghetto_csv = open("results/layout_results.csv", "w")

# write labels
label_lst = ["layout"]
for i in range(101):
    label_lst.append(str(i/100.0))
    label_str = ",".join(label_lst)
ghetto_csv.write(label_str)
ghetto_csv.write("\n")

# write data
for layout, row in layout_results.iteritems():
    sorted_layout_results = [str(layout)]
    for ambiguity_count in range(101):
        sorted_layout_results.append(str(row[ambiguity_count/100.0]))
        string_results = ",".join(sorted_layout_results)
    ghetto_csv.write(string_results)
    ghetto_csv.write("\n")
ghetto_csv.close()