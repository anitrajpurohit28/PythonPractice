# 9 Python program to count number of vowels using sets in given string

input1 = "This is a sample string"
input2 = "other string"


def vowel_count_set(string):
    count = 0
    vowel_set = set("aeiouAEIOU")
    for char in string:
        if char in vowel_set:
            count += 1
    print(f"Vowel count: {count}")


vowel_count_set(input1)
vowel_count_set(input2)

print("-----individual count ----")
def vowel_count_individual_count(string):
    string = string.lower()
    count = 0
    count = string.count('a') + string.count('e') + \
            string.count('i') + string.count('o') + \
            string.count('u')
    print(f"Vowel count: {count}")


vowel_count_individual_count(input1)
vowel_count_individual_count(input2)
