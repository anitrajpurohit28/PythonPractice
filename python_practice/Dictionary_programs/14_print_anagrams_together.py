# 14 Print anagrams together in Python using List and Dictionary

arr = ['cat', 'dog', 'tac', 'god', 'act']

# 1. use sorted word as key to insert all the words into list
# 2. Print all the values of key, one by by
def print_anagrams_together(inp):
    dict_words = {}
    for str_val in arr:
        key = "".join(sorted(str_val))
        # insert all the words to dictionary
        if key in dict_words.keys():
            dict_words[key].append(str_val)
        else:
            dict_words[key] = []
            dict_words[key].append(str_val)

    print(dict_words)

    output = ""
    for k, v in dict_words.items():
        output = output + " ".join(v) + " "
    print(output)

print_anagrams_together(arr)
