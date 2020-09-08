# 10 Remove all duplicates from a given string in Python
input1 = 'aabbcccddekll12@aaeebbbb'
print(input1)

# by using set; unordered
print("----unordered set------")
def remove_duplicates_set(string):
    unique_chars = set(string)
    print(''.join(unique_chars))

remove_duplicates_set(input1)

print("----OrderedDict------")

# by using set; ordered dictionary
from collections import OrderedDict

def remove_duplicates_orderedDict(string):
    unique_chars = OrderedDict.fromkeys(string)
    print(''.join(unique_chars))

remove_duplicates_orderedDict(input1)

print("---new string---")
def remove_duplicate_naive(string):
    result_str = ""
    for char in string:
        if char in result_str:
            pass
        else:
            result_str +=char
    print(result_str)
remove_duplicate_naive(input1)

print("----new list ------")

def remove_duplicate_list(string):
    unique_list = []
    for i in string:
        if i not in unique_list:
            unique_list.append(i)
    print("".join(unique_list))

remove_duplicate_list(input1)

print("----overwrite string ------")

def remove_duplicate_no_extra_space(string):
    r, w = 0, 0
    while r < len(string):
        if string[r] not in string[:r]:
            string[w] = string[r]
            r += 1
            w += 1
        else:
            string[w] = string[r]
            r += 1
    string = string[:w]
    # OR
    # del string[w:]
    print("".join(string))

remove_duplicate_no_extra_space(list(input1))

