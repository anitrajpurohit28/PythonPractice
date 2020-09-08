# 7 Python | Program to accept the strings which contains all vowels

input1 = "This is a input string; vowels are"
input2 = "other string"


def check_if_vowels_present_set_method(string):
    input_string = string.lower()
    vowels = set("aeiou")
    found_vowels = set()
    for char in input_string:
        if char in vowels:
            found_vowels.add(char)
        else:
            pass

    if len(found_vowels) == len(vowels):
        print("found all vowels in str")
    else:
        print("not accepted")


check_if_vowels_present_set_method(input1)
check_if_vowels_present_set_method(input2)


print("----Count method ----")
def check_if_vowels_present_count_method(string):
    input_string = string.lower()
    # build list with count of each vowel
    vowel = [string.count('a'), string.count('e'),
             string.count('i'), string.count('o'),
             string.count('u')]
    print(vowel)
    if vowel.count(0) == 0:
        print("found all vowels in str")
    else:
        print("not accepted")


check_if_vowels_present_count_method(input1)
check_if_vowels_present_count_method(input2)
