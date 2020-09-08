# 22 Python program to print negative numbers in a list
# 24 Python program to print all negative numbers in a range

import random
start_range = -200
end_range = 200
list1 = random.sample(range(start_range, end_range), 20)
print(list1)

# for loop
negative_list = []
for num in list1:
    if num < 0:
        negative_list.append(num)

print(negative_list)

# while loop
negative_list = []
num = 0
while num < len(list1):
    if list1[num] < 0:
        negative_list.append(list1[num])
    num += 1

print(negative_list)

# list comprehension
negative_list = []
negative_list = [num for num in list1 if num < 0]
print(negative_list)

# lambda
negative_list = []
negative_list = list(filter(lambda x: x < 0, list1))
print(negative_list)
