from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    word_list = []
    for i in range(0, len(string), k):
        word_list.append(string[i:i + k])

    for word in word_list:
        print("".join(OrderedDict.fromkeys(word)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
