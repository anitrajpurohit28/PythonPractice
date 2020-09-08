# 13 Find words which are greater than given length k
word_len = 4
input1 = "This is a sample string"


def print_words_greater_than(input_str, length):
    split_words = input_str.split(" ")
    result = []
    for word in split_words:
        if len(word) > length:
            result.append(word)
    return result


res = print_words_greater_than(input1, word_len)
print(res)
