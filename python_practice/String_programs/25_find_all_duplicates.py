# 25 Python Counter| Find all duplicate characters in string

from collections import Counter

input1 = 'geeksforgeeks'
input2 = "thisisasamplestring"


def find_duplicates(input_str):
    # Counter will return a dictionary with
    # char as key and occurrence as value
    word_counter = Counter(input_str)
    print(word_counter)
    index = -1
    for value in word_counter.values():
        index = index+1
        if value > 1:
            print(list(word_counter.keys())[index], end=' ')


find_duplicates(input1)
find_duplicates(input2)
