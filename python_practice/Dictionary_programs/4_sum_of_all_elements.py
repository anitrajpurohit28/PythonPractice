# 4 Python program to find the sum of all items in a dictionary

dict1 = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}


def sum_dict_values(input_dict):
    dict_sum = 0
    for index in dict1.values():
        dict_sum += index
    return dict_sum
print("dict.values: ", sum_dict_values(dict1))


def sum_dict_subscript(input_dict):
    dict_sum = 0
    for index in dict1:
        dict_sum += dict1[index]
    return dict_sum
print("dict[index]: ", sum_dict_subscript(dict1))

def sum_dict_sum_func(input_dict):
    dict_sum = sum(input_dict.values())
    return dict_sum
print("sum function: ", sum_dict_sum_func(dict1))
