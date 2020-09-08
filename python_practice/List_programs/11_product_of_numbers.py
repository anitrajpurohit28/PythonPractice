# 11 Python | Multiply all numbers in the list

list1 = list(range(1, 11))


def multiply_list(input_list):
    result = 1
    for element in input_list:
        result *= element
    return result


res = multiply_list(list1)
print(f"Product: {res}")


import numpy

res = numpy.prod(list1)
print(f"Product: {res}")


from functools import reduce

res = reduce(lambda x, y: x * y, list1)
print(f"Product: {res}")

