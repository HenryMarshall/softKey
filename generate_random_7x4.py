from random import shuffle
import sys

# generates 7 x 4

chars = "abcdefghijklmnopqrstuvwxyz.'"
char_list = list(chars)

random_layouts = {}

for i in range(int(sys.argv[1])):
  shuffle(char_list)
  layout = []

  for row_count in range(4):
    row = char_list[row_count*7:row_count*7+7]
    layout.append(row)

  random_layouts[i] = layout

print random_layouts