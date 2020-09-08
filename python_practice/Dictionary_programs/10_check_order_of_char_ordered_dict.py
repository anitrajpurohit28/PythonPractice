# 10 Python | Check order of character in string using OrderedDict( )

"""
Input:
string = "engineers rock"
pattern = "er";
Output: true
Explanation:
All 'e' in the input string are before all 'r'.

Input:
string = "engineers rock"
pattern = "egr";
Output: false
Explanation:
There are two 'e' after 'g' in the input string.

Input:
string = "engineers rock"
pattern = "gsr";
Output: false
Explanation:
There are one 'r' before 's' in the input string.
"""

from collections import OrderedDict


def check_order_ordered_dict(input_str, pattern):
    dict1 = OrderedDict.fromkeys(input_str)
    pattern_match = 0
    for key, value in dict1.items():
        if key == pattern[pattern_match]:
            pattern_match += 1
        if pattern_match == len(pattern):
            return True

    return False


def check_order_naive(input_str, pattern):
    for i in range(len(pattern)-1):
        x = pattern[i]
        # range is run till pattern len -1 to take care of
        # Index Error
        y = pattern[i+1]

        # Now, check last occurrence of x should be lesser
        # than first occurrence of y
        x_last = input_str.rindex(x)
        y_first = input_str.index(y)
        if x_last == -1 or y_first == -1 or x_last > y_first:
            return False

    return True


input_str = 'engineers rock'
pattern = 'er'
print(f"input_str: {input_str}\n"
      f"pattern: {pattern}\n"
      f"result:")
print("Ordered dict:", check_order_ordered_dict(input_str, pattern))
print("Naive:", check_order_naive(input_str, pattern))
print()


input_str = 'engineers rock'
pattern = 'egr'
print(f"input_str: {input_str}\n"
      f"pattern: {pattern}\n"
      f"result:")
print("Ordered dict:", check_order_ordered_dict(input_str, pattern))
print("Naive:", check_order_naive(input_str, pattern))
print()

input_str = 'engineers rock'
pattern = 'gsr'
print(f"input_str: {input_str}\n"
      f"pattern: {pattern}\n"
      f"result:")
print("Ordered dict:", check_order_ordered_dict(input_str, pattern))
print("Naive:", check_order_naive(input_str, pattern))
print()
