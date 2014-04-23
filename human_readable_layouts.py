layouts = {

    # layouts developed for hardware keyboards

    'qwerty':
        # replaced ";" with "'"
        [["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
         ["a", "s", "d", "f", "g", "h", "j", "k", "l", "'"],
         ["z", "x", "c", "v", "b", "m", "n", ",", ".", "/"]],

    'colemak':
        # replaced ";" with "'"
        [["q", "w", "f", "p", "g", "j", "l", "u", "y", "'"],
         ["a", "r", "s", "t", "d", "h", "n", "e", "i", "o"],
         ["z", "x", "c", "v", "b", "k", "m", ",", ".", "/"]],

    'dvorak':
        # replaced ";" with "/"
        [["'", ",", ".", "p", "y", "f", "g", "c", "r", "l"],
         ["a", "o", "e", "u", "i", "d", "h", "t", "n", "s"],
         ["/", "q", "j", "k", "x", "b", "m", "w", "v", "z"]],

    'dvorak1H':
        # moved "z" from right of "a" to position of ","
        # replaced "]" with "'"
        # replaced "/" with "."
        [["'", ".", "p", "f", "m", "l", "j"],
         ["q", "b", "y", "u", "r", "s", "o"],
         ["k", "c", "d", "t", "h", "e", "a"],
         ["x", "g", "v", "w", "n", "i", "z"]],
    
    
    # layouts developed for software keyboards
    
    'opti': 
        # when converted to key_position, last space (" ") will be used
        # replaced upper left space with "." and "'"
        [["q", "f", "u", "m", "c", "k", "z"],
         [".", "'", "o", "t", "h", " ", " "],
         ["b", "s", "r", "e", "a", "w", "x"],
         [" ", " ", "i", "n", "d", " ", " "],
         ["j", "p", "v", "g", "l", "y", "'"]],
    
    'fitaly':
        # when converted to key_position, last space (" ") will be used
        # replaced left space with "." and "'"
        [["z", "v", "c", "h", "w", "k"],
         ["f", "i", "t", "a", "l", "y"],
         [".", "'", "n", "e", " ", " "],
         ["g", "d", "o", "r", "s", "b"],
         ["q", "j", "u", "m", "p", "x"]]

}


# templates

# templates = {

#     '10x3':  
#         [["", "", "", "", "", "", "", "", "", ""],
#          ["", "", "", "", "", "", "", "", "", ""],
#          ["", "", "", "", "", "", "", "", "", ""]],

#     '7x4':   
#         [["", "", "", "", "", "", ""],
#          ["", "", "", "", "", "", ""],
#          ["", "", "", "", "", "", ""],
#          ["", "", "", "", "", "", ""]]

# }
