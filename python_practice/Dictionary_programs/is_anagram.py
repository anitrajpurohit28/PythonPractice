inp1a = "geeksforgeeks"
inp1b = "forgeeksgeeks"

inp2a = "testabc"
inp2b = "xyztest"

from collections import Counter
def is_anagram_counter(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    if dict1 == dict2:
        res = "anagram"
    else:
        res = "NOT anagram"
    print(f"{str1} and {str2} are ==> {res}")

def is_anagram_str_sort(str1, str2):
    sorted_list1 = sorted(str1)
    sorted_list2 = sorted(str2)
    if sorted_list1 == sorted_list2:
        res = "anagram"
    else:
        res = "NOT anagram"
    print(f"{str1} and {str2} are ==> {res}")

is_anagram_counter(inp1a, inp1b)
is_anagram_str_sort(inp1a, inp1b)

is_anagram_counter(inp2a, inp2b)
is_anagram_str_sort(inp2a, inp2b)