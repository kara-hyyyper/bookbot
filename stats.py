# -- FUNCTIONS ------------------------------

def get_word_count(contents):
    contents_arr = contents.split()

    return len(contents_arr)

def get_char_count(contents):
    contents_lowercase = contents.lower()
    char_count_dict = {}

    for char in contents_lowercase:
        if char in char_count_dict:
            count = char_count_dict[char]
            char_count_dict[char] = count+1
        else:
            char_count_dict[char] = 1

    return char_count_dict
