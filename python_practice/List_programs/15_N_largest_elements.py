# 15 Python program to find N largest elements from a list

import random
import unittest
list1 = random.sample(range(1, 300), 11)
print(list1)
n = 4

# using sort and print last N items using slice operator
temp_list = sorted(list1)
res1_list = temp_list[-n:]
print(res1_list)


# calculate manually

def n_max_elements(temp_list, n):
    result_list = []
    for i in range(n):
        max1 = temp_list[0]
        for j in range(len(temp_list)):
            if temp_list[j] > max1:
                max1 = temp_list[j]

        temp_list.remove(max1)
        result_list.append(max1)

    return result_list


res2_list = n_max_elements(list1[:], n)
print(res2_list)

res1_list.sort()
res2_list.sort()

assert res1_list == res2_list
