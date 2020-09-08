import random
import pickle

lower = 1
higher = 900000000
arr_len = 20000000

# with open("sorted_array.pickle", "wb") as arr_file:
#     arr = []
#     for _ in range(arr_len):
#         arr.append(random.randint(lower, higher))
#     arr.sort()
#     #arr_file.write(arr)
#     pickle.dump(arr, arr_file)

with open("sorted_array.pickle", "rb") as arr_file:
    arr = pickle.load(arr_file)
    print(type(arr))

for i in range(100):
    print(arr[i])
