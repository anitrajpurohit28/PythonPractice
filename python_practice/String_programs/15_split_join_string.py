# 15 Python program to split and join a string

input1 = "This is a sample string"
print(f"Input: {input1}")


def split_string(input_str, delimiter= " "):
    return input_str.split(delimiter)


def join_string(input_str, delimiter = " "):
    return delimiter.join(input_str)


split_list = split_string(input1, " ")
print(split_list)

join_str = join_string(split_list, " ")
print(join_str)
