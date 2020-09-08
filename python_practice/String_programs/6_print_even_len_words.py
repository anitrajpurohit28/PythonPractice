# 6 Python program to print even length words in a string

input1 = "This is a python language"

word_list = input1.split(' ')
print(word_list)

for word in word_list:
    if len(word) % 2 == 0:
        print(word)
