import human_readable_layouts
import pickle

hr_layouts = human_readable_layouts.layouts
key_position = {}

for layout in hr_layouts:
    key_position[layout] = {}

    for row_num, row in enumerate(hr_layouts[layout]):
        for col_num, char in enumerate(row):
            key_position[layout][char] = {
                'x': col_num,
                'y': row_num
            }

print key_position

with open('character_positions.pickle', 'wb') as handle:
    pickle.dump(key_position, handle)