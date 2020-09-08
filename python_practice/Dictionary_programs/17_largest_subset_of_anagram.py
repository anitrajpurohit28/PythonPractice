# 17 Python Counter to find the size of largest subset of anagram words

"""
Input:
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3

Input:
cars bikes arcs steer
Output: 2
"""

input_str = 'ant magenta magnate tan gnamate '
input_str2 = 'an na tomato otatom naman manan nanam amann'
from collections import Counter


def max_anagram_size(input_str):
    input_list = input_str.split(" ")
    sorted_input_list = []
    for word in input_list:
        sorted_input_list.append(''.join(sorted(word)))

    # print(sorted_input_list)  # this is for debugging only

    # by now, all the input words are sorted.
    # all the anagram strings would be looking alike
    frequency_dict = Counter(sorted_input_list)
    print(frequency_dict)
    print(f"Anagram with max occurance is {max(frequency_dict.values())}")


max_anagram_size(input_str)
max_anagram_size(input_str2)