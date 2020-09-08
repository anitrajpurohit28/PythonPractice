# 23 Python dictionary, set and counter to check if frequencies can become same
str1 = "xxxxyyzz"
str2 = "xxyy"
from collections import Counter

def freq_of_char_all_same_off_by_one(input_str):
    freq_dict = Counter(input_str)
    value_list = list(set(freq_dict.values()))
    print(value_list)
    if len(value_list) > 2:
        print("No")
    elif 2 == len(value_list) and abs(value_list[0] - value_list[1]) > 1:
        print("No")
    else:
        print("Yes")


freq_of_char_all_same_off_by_one(str1)
freq_of_char_all_same_off_by_one(str2)
