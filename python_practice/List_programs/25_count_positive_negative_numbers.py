# 25 Python program to count positive and negative numbers in a list

import random
start_range = -200
end_range = 200
list1 = random.sample(range(start_range, end_range), 20)
print(list1)
# for loop
positive_count = 0
negative_count = 0
for num in list1:
    if num >= 0:
        positive_count += 1
    else:
        negative_count += 1
print(f"Positive count: {positive_count}\tNegative count: {negative_count}")

# while loop
positive_count = 0
negative_count = 0
num = 0
while num < len(list1):
    if list1[num] >= 0:
        positive_count += 1
    else:
        negative_count += 1
    num += 1
print(f"Positive count: {positive_count}\tNegative count: {negative_count}")


# list comprehension
positive_count = len([num for num in list1 if num >= 0])
negative_count = len([num for num in list1 if num < 0])
print(f"Positive count: {positive_count}\tNegative count: {negative_count}")

# lambda + filter
positive_count = len(list(filter(lambda x: x >= 0, list1)))
negative_count = len(list(filter(lambda x: x < 0, list1)))
print(f"Positive count: {positive_count}\tNegative count: {negative_count}")

