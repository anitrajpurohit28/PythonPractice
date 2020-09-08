# 15 K’th Non-repeating Character in Python using List Comprehension and OrderedDict

inp1 = "geeksforgeeks"
k = 2
from collections import OrderedDict

def kth_non_repeating_char(input_str, key):
    order_dict = OrderedDict.fromkeys(input_str, 0)
    for char in input_str:
        order_dict[char] += 1
    print(order_dict)

    non_repeated_list = []
    for k, v in order_dict.items():
        if v == 1:
            non_repeated_list.append(k)

    print(non_repeated_list)
    if key > len(non_repeated_list):
        print("Non repeated elements are less than k")
    else:
        print(non_repeated_list[key])


kth_non_repeating_char(inp1, k)
