import random
import pickle

lower = 1
higher = 900000000
arr_len = 50000000

arr = []
for _ in range(arr_len):
    arr.append(random.randint(lower, higher))
arr.sort()

#print(arr)
with open("sorted_array.txt", "w") as arr_file:
    arr_file.write("\n".join(str(element) for element in arr))

# with open("sorted_array.txt", "r") as arr_file:
#     data = arr_file.readlines()

# for line in data:
#     print(line.strip())
print("Done")