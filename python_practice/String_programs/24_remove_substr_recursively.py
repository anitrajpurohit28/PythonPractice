# 24 String slicing in Python to check if a string can become empty by recursive deletion

input1 = "GEEGEEKSKS"
pattern = "GEEKS"

input2 = "GEEKGEEKSKS"
pattern = "GEEKS"


def remove_till_empty(input_str, sub_str):
    if len(input_str) == 0 and len(sub_str) == 0:
        return True

    if len(pattern) == 0:
        return True

    while len(input_str):
        index = input_str.find(sub_str)

        if index == -1:
            return False

        input_str = input_str[:index] + input_str[index+len(sub_str):]
        print(input_str)




res = remove_till_empty(input1, pattern)
print(res)

res = remove_till_empty(input2, pattern)
print(res)
