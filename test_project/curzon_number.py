from unittest import *
def is_curzon(num):
    exp = (2 ** num) + 1
    mul = (2 * num) + 1
    if exp % mul == 0:
        return True
    return False

def is_curzon2(num):
    return ((2 ** num) + 1) % ((2 * num) + 1) == 0



print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))

print(is_curzon2(5))
print(is_curzon2(10))
print(is_curzon2(14))
