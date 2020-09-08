# 26 Remove multiple elements from a list in Python


# delete all even numbers from list
list1 = [11, 5, 17, 18, 23, 50]

print(f"Before operation: {list1}")
for element in list1:
    if element % 2 == 0:
        list1.remove(element)
print(f"After operation:  {list1}")

# delete all even numbers by crating new list
# using list comprehension
list1 = [11, 5, 17, 18, 23, 50]

print(f"Before operation: {list1}")
list1 = [num for num in list1 if num % 2 != 0]
print(f"After operation:  {list1}")


# remove by index using slicing
# from from index 1 to 4
list1 = [11, 5, 17, 18, 23, 50]

print(f"Before operation: {list1}")
del list1[1:5]
print(f"After operation:  {list1}")

# remove elements using list comprehension
list1 = [11, 5, 17, 18, 23, 50]
unwanted_numbers = [11, 5]
print(f"Before operation: {list1}")
list1 = [num for num in list1 if num not in unwanted_numbers]
print(f"After deleting {unwanted_numbers}:  {list1}")

# remove elements by index
list1 = [11, 5, 17, 18, 23, 50]
print(f"Before operation: {list1}")
# removes 11, 18, 23
unwanted_index = [0, 3, 4]
# need to reverse the index so that when we delete higher index
# lower index doesn't change.
# if we start deleting from lower index, the index of numbers
# will change
for del_index in sorted(unwanted_index, reverse=True):
    del list1[del_index]
print(f"After deleting index {unwanted_index}:  {list1}")
