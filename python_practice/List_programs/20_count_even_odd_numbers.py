# 20 Python program to count Even and Odd numbers in a List

list1 = list(range(1, 21))
print(list1)

even_count, odd_count = 0, 0

# for loop
for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even: {even_count} Odd: {odd_count}")

# while loop
even_count, odd_count = 0, 0
num = 0
while num < len(list1):
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num += 1
print(f"Even: {even_count} Odd: {odd_count}")

# list comprehension
even_list = [num for num in list1 if num % 2 == 0]
even_count = len(even_list)
odd_count = len(list1) - even_count
print(f"Even: {even_count} Odd: {odd_count}")

#  lambda
odd_count = len(list(filter(lambda x: x % 2 == 0, list1)))
event_count = len(list(filter(lambda x: x % 2 != 0, list1)))
print(f"Even: {even_count} Odd: {odd_count}")
