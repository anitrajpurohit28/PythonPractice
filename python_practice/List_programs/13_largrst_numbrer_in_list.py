# 13 Python program to find largest number in a list


import random

# generate list of random numbers by sample
list1 = random.sample(range(1, 300), 10)
print(list1)

largest = max(list1)
print(f"Largest: {largest}")

temp_list = sorted(list1)
largest = temp_list[-1]
print(f"Largest: {largest}")


large = list1[0]
index = 0

while index < len(list1):
    if large < list1[index]:
        large = list1[index]
    index += 1
large = temp_list[-1]
print(f"Largest: {large}")


large = list1[0]
index = 0
for index in range(len(list1)):
    if large < list1[index]:
        large = list1[index]

large = temp_list[-1]
print(f"Largest: {large}")

