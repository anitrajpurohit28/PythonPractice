# 17 Python | Find all close matches of input string from a list

from difflib import get_close_matches

def close_match(input_string, patterns):
    print(get_close_matches(input_string, patterns))


patterns = ['ape', 'apple', 'peach', 'puppy']
close_match("appel", patterns)
