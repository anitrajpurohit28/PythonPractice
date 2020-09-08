# 19 Python Dictionary to find mirror characters in a string


def mirror_char_dict(input_str, k):
    original = "abcdefghijklmnopqrstuvwxyz"
    reverse = original[::-1]
    dict_char = dict(zip(original, reverse))
    # print(dict_char)
    prefix = input_str[:k]
    suffix = input_str[k:]
    mirror = ""
    for i in range(len(suffix)):
        mirror = mirror + dict_char[suffix[i]]
    output = prefix + mirror
    print(output)


def mirror_char_ord(input_str, k):
    original = "abcdefghijklmnopqrstuvwxyz"
    reverse = original[::-1]
    prefix = input_str[:k]
    suffix = input_str[k:]
    mirror = ''
    for i in range(len(suffix)):
        mirror += reverse[ord(suffix[i])-ord('a')]
    output_str = prefix + mirror
    print(output_str)



inp1 = 'paradox'
k = 3
mirror_char_dict(inp1, k)
mirror_char_ord(inp1, k)
