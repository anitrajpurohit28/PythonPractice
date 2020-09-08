# 2 Reverse words in a given String in Python

input1 = "geeks quiz practice code"

def reverse_words(sentence):
    words = sentence.split(' ')
    rev_words = ' '. join(reversed(words))
    print(rev_words)


reverse_words(input1)
