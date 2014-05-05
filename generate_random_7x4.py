import sys
import calc_char_positions
import pickle
import time
from random import shuffle

# generates 7 x 4

chars = "abcdefghijklmnopqrstuvwxyz.'"
char_list = list(chars)

random_layouts_human = {}
random_layouts_computer = {}

for i in range(int(sys.argv[1])):
    shuffle(char_list)
    layout = []

    # todo: change jump amount, improve readability of selector
    for row_count in range(4):
        row = char_list[row_count*7:row_count*7+7]
        layout.append(row)

    random_layouts_human[i] = layout

    computer_readable = calc_char_positions.human_layout_to_computer(layout)
    random_layouts_computer[i] = computer_readable

# store layouts in pickle
file_name = "%i_random.pickle" % time.time()
with open('human_layouts/' + file_name, 'wb') as handle:
    pickle.dump(random_layouts_human, handle)
with open('computer_layouts/' + file_name, 'wb') as handle:
    pickle.dump(random_layouts_computer, handle)