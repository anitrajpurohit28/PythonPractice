# 25 Possible Words using given characters in Python

from collections import Counter
input_str_list = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
char_set = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

def possible_words_counter(input_str_list, char_set):
    not_possible_list = []
    possible_list = []

    for word in input_str_list:
        char_dict = Counter(word)
        # char_dict will contain each frequency of each character
        # of word

        flag = True
        for char in char_dict.keys():
            if char not in char_set:
                flag = False

        if flag:
            possible_list.append(word)
        else:
            not_possible_list.append(word)


    print("Possible: ", possible_list)
    print("Not possible_list: ", not_possible_list)

possible_words_counter(input_str_list, char_set)
