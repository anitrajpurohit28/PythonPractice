# 22 Python counter and dictionary intersection example (Make a string using deletion and rearrangement)

"""
Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : Not Possible

Input : s1 = GeeksforGeeks
      : s2 = rteksfoGrdsskGeggehes
Output : Possible
"""

s1a = "ABHISHEKsinGH"
s2a = "gfhfBHkooIHn987ghjiuygfvbnj98uyfnAAdSHEKsiAnG"

s1b = "Hello"
s2b = "dnaKfhelddf"

s1c = "GeeksforGeeks"
s2c = "rteksfoGrdsskGeggehes"


def possible_to_make_str_naive(s1, s2):
    print("possible_to_make_str_naive", end=':  ')

    flag = 1
    for char in s1:
        if char not in s2:
            flag = 0
            break

    if flag == 1:
        print("possible")
    else:
        print("Not possible")

from collections import Counter

def possible_to_make_str_counter(s1, s2):
    print("possible_to_make_str_counter", end=':  ')
    dict1 = Counter(s1)
    dict2 = Counter(s2)

    intersection = dict1 & dict2

    if intersection == dict1:
        print("possible")
    else:
        print("Not possible")

print("s1: ", s1a)
print("s2: ", s2a)
possible_to_make_str_naive(s1a, s2a)
possible_to_make_str_counter(s1a, s2a)

s1 = s1b
s2 = s2b
print("s1: ", s1)
print("s2: ", s2)
possible_to_make_str_naive(s1, s2)
possible_to_make_str_counter(s1, s2)

s1 = s1c
s2 = s2c
print("s1: ", s1)
print("s2: ", s2)
possible_to_make_str_naive(s1, s2)
possible_to_make_str_counter(s1, s2)

