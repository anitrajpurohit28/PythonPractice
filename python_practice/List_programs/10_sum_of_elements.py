# 10 Python program to find sum of elements in list

list1 = list(range(1, 11))

total = 0
for element in list1:
    total += element

print(f"Sum = {total}")


total = 0
index = 0

while index < len(list1):
    total += list1[index]
    index += 1

print(f"Sum = {total}")


def sum_of_list(input_list, size):
    if size == 0:
        return 0
    else:
        return input_list[size-1] + sum_of_list(input_list, size-1)


total = sum_of_list(list1, len(list1))
print(f"Sum = {total}")



total = sum(list1)
print(f"Sum = {total}")

