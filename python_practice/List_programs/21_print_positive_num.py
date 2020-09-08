# 21 Python program to print positive numbers in a list
# 23 Python program to print all positive numbers in a range
import random

start_range = -200
end_range = 200
list1 = random.sample(range(start_range, end_range), 20)
print(list1)

# for loop
positive_list = []
for num in list1:
    if num >= 0:
        positive_list.append(num)

print(positive_list)

# while loop
positive_list = []
num = 0
while num < len(list1):
    if list1[num] >= 0:
        positive_list.append(list1[num])
    num += 1

print(positive_list)

# list comprehension
positive_list = []
positive_list = [num for num in list1 if num >= 0]
print(positive_list)

# lambda
positive_list = []
positive_list = list(filter(lambda x: x >= 0, list1))
print(positive_list)
