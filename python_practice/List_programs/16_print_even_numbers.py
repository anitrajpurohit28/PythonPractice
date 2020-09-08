# 16 Python program to print even numbers in a list

list1 = list(range(1, 11))
print(list1)

# FOR loop
temp_list = []
for num in list1:
    if num % 2 == 0:
        temp_list.append(num)
print(temp_list)

# WHILE loop
i = 0
temp_list = []
while i < len(list1):
    if list1[i] % 2 == 0:
        temp_list.append(list1[i])
    i += 1
print(temp_list)

# list comprehension
even_only = [num for num in list1 if num % 2 == 0]
print(even_only)


# lambda + filter
even_only = []
even_only = list(filter(lambda x: (x % 2 == 0), list1))
print(even_only)
