# 8 Python | Count the Number of matching characters in a pair of string

input1 = 'aabbcccddekll12@'
input2 = 'bb22ll@55k'

input3 = "abcdef"
input4 = "defghia"

# set + if char match, append in list
def no_of_matching_chars_in_str_pair(string1, string2):
    count = 0
    set1 = set(string1)
    set2 = set(string2)
    match_char = []
    for char in set1:
        if char in set2:
            match_char.append(char)
            count += 1
    print(f"Number of Match chars: {count}\n{match_char}")


no_of_matching_chars_in_str_pair(input1, input2)
no_of_matching_chars_in_str_pair(input3, input4)

print("-----set intersection method------")

# set intersection
def no_of_matching_chars_in_str_pair_set_intersection(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    match_char = set1 & set2
    count = len(match_char)
    print(f"Number of Match chars: {count}\n{match_char}")


no_of_matching_chars_in_str_pair(input1, input2)
no_of_matching_chars_in_str_pair(input3, input4)

print("----- string.find------")

def no_of_matching_chars_in_str_pair_find(string1, string2):
    count = 0
    match_char = []
    for char in string1:
        if -1 != string2.find(char):
            if char not in match_char:
                match_char.append(char)
                count += 1
    print(f"Number of Match chars: {count}\n{match_char}")



no_of_matching_chars_in_str_pair_find(input1, input2)
no_of_matching_chars_in_str_pair_find(input3, input4)


print("----- string.search------")
import re
def no_of_matching_chars_in_str_pair_search(string1, string2):
    count = 0
    match_char = []
    for char in string1:
        if re.search(char, string2):
            if char not in match_char:
                match_char.append(char)
                count += 1
    print(f"Number of Match chars: {count}\n{match_char}")



no_of_matching_chars_in_str_pair_search(input1, input2)
no_of_matching_chars_in_str_pair_search(input3, input4)


def count(str1, str2):
    count, j = 0, 0
    for i in str1:
        # logic of j is j is an iterator counter;
        # find returns 1st found index.
        # if found j == index, this is the index
        # both find points to, and we are at it
        # else, we have already passed by this character
        # but still find it pointing there. Lets not
        # consider that.
        if str2.find(i) >= 0 and j == str1.find(i):
            count += 1
        j += 1
    print('No. of matching characters are : ', count, j)

count(input1, input2)
count(input3, input4)

print(input1.find('a'))
