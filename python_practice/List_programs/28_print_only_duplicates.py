# 28 Python | Program to print duplicates from a list of integers
import random
list1 = [random.randint(1, 5) * 10 for i in range(10)]
print(list1)

# list elements which are duplicated
duplicate_list = list(filter(lambda x: list1.count(x) > 1, list1))
# only the duplicate elements
duplicates = set(duplicate_list)
print(duplicates)

# OR
duplicates = set(list(filter(lambda x: list1.count(x) > 1, list1)))
print(duplicates)

duplicate_list = []
for element in list1:
    if list1.count(element) > 1 and element not in duplicate_list:
        duplicate_list.append(element)

print(duplicate_list)

# manually calculated
def duplicate_list(list1):
    repeated = []
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] == list1[j] and list1[i] not in repeated:
                repeated.append(list1[i])
    return repeated


repeated_list = duplicate_list(list1)
print(repeated_list)

