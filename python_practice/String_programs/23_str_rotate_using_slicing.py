# 23 String slicing in Python to rotate a string

input1 = "ABCdefGHI"
rotate_no = 3
def str_rotate_right_split(input_str, rotate_no):
    result = input_str[rotate_no:] + input_str[:rotate_no]
    return result


def str_rotate_left_split(input_str, rotate_no):
    result = input_str[-rotate_no:] + input_str[:-rotate_no]
    return result


res = str_rotate_right_split(input1, rotate_no)
print(f"Input str: {input1}\nRight rotate str: {res}")

res = str_rotate_left_split(input1, rotate_no)
print(f"Input str: {input1}\nLeft rotate str: {res}")



