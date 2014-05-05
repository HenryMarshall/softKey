def human_layout_to_computer(human_layout):
    computer_layout = {}
    for row_num, row in enumerate(human_layout):
        for col_num, char in enumerate(row):
            computer_layout[char] = {
                'x': col_num,
                'y': row_num
            }
    return computer_layout