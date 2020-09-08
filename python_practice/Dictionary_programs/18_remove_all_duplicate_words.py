# 18 Python | Remove all duplicates words from a given sentence

input1 = "Python is great and Java is also great"
input2 = "Geeks for Geeks"


def remove_duplicate_simple(input_str):
    input_list = input_str.split(" ")
    new_str_list = []
    for string in input_list:
        if string not in new_str_list:
            new_str_list.append(string)

    new_str_list = " ".join(new_str_list)
    return new_str_list


from collections import Counter

def remove_duplicate_counter(input_str):
    # split individual words into list
    new_str_list = input_str.split(" ")
    # Count occurrence if each word in list
    new_str_dict = Counter(new_str_list)
    unique_words = new_str_dict.keys()
    unique_words_str = " ".join(unique_words)
    return unique_words_str


output = remove_duplicate_simple(input1)
print(f"remove_duplicate_simple:\ninput: {input1}|\t|output: {output}")

output = remove_duplicate_counter(input1)
print(f"remove_duplicate_counter:\ninput: {input1}|\t|output: {output}")

output = remove_duplicate_simple(input2)
print(f"remove_duplicate_simple:\ninput: {input2}|\t|output: {output}")

output = remove_duplicate_counter(input2)
print(f"remove_duplicate_counter:\ninput: {input2}|\t|output: {output}")
