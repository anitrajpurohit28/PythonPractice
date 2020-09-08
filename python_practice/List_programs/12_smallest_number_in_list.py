# 12 Python program to find smallest number in a list

import random

# generate list of random numbers by sample
list1 = random.sample(range(1, 300), 10)
print(list1)


smallest = min(list1)
print(f"Smallest: {smallest}")


temp_list = sorted(list1)
# print(temp_list)
smallest = temp_list[0]
print(f"Smallest: {smallest}")


minimum = list1[0]
for i in range(len(list1)):
    if list1[i] < minimum:
        minimum = list1[i]
print(f"Smallest: {minimum}")

