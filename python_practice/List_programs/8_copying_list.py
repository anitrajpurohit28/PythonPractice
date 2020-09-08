# 8 Python | Cloning or Copying a list
import time

input_list = list(range(1, 20000))

print("------using slicing technique------")
start_time = time.time()
li_copy = input_list[:]
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")


print("------using extend method ------")

start_time = time.time()
li_copy = []
li_copy.extend(input_list)
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")

print("------using builtin list ------")

start_time = time.time()
li_copy = list(input_list)
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")

print("------using iter to copy individual elements ------")
start_time = time.time()
li_copy = []
for i in input_list:
    li_copy.append(i)
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")

print("------using list comprehension ------")
start_time = time.time()
li_copy = [i for i in input_list]
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")


print("------using builtin copy() ------")
start_time = time.time()
li_copy = []
li_copy = input_list.copy()
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")

print("-----using shallow copy method ------")
import copy

start_time = time.time()
li_copy = copy.copy(input_list)
li_copy = input_list.copy()
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")


print("-----using deep copy method ------")
import copy

start_time = time.time()
li_copy = copy.deepcopy(input_list)
li_copy = input_list.copy()
end_time = time.time()
time_taken = end_time - start_time
if li_copy == input_list:
    print(f"Passed: Time taken: {time_taken} seconds")
else:
    print("Failed")
