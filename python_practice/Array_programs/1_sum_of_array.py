# 1. Python Program to find sum of array

arr1 = [12, 3, 4, 15]

def sum_of_array(inp_arr):
    sum = 0
    for item in inp_arr:
        sum += item
    return sum

print(sum_of_array(arr1))
print(sum(arr1))
