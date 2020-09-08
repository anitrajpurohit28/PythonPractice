# 14 Python program to find second largest number in a list
import random
list1 = random.sample(range(1, 300), 11)
print(list1)

# by sorting
temp_list = sorted(list1)
first_max = temp_list[-1]
sec_max = temp_list[-2]
print(f"First Largest: {first_max}\tSecond Largest: {sec_max}")

# By manually calculating
first_max = list1[0]
sec_max = list1[1]
if sec_max > first_max:
    first_max, sec_max = sec_max, first_max

for i in range(2, len(list1)):
    if list1[i] > first_max:
        sec_max = first_max
        first_max = list1[i]
    elif list1[i] > sec_max and list1[i] != first_max:
        sec_max = list1[i]
    else:
        pass
        # case where first and second are both same numbers
        # if sec_max == first_max:
        #    sec_max = list1[i]
print(f"First Largest: {first_max}\tSecond Largest: {sec_max}")


# by removing max element
first_max = max(list1)
temp_list = list1.remove(max(list1))
sec_max = max(list1)
print(f"First Largest: {first_max}\tSecond Largest: {sec_max}")

