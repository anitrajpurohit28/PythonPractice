# 13 Find all duplicate characters in string

from collections import Counter
input1 = "GeeksForGeeks"


def print_all_duplicate_char(input1):
    char_count_dict = Counter(input1)

    for key, value in char_count_dict.items():
        if value > 1:
            print(f"{key} -> {value}")


def print_all_duplicate_char_by_values(input1):
    char_count_dict = Counter(input1)
    print([(k, v) for k, v in char_count_dict.items() if v > 1])


print_all_duplicate_char(input1)
print_all_duplicate_char_by_values(input1)