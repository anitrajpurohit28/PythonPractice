# 5 Python | Ways to check if element exists in list
import time

test_list = list(range(1, 20001))
second_list = list(range(15000, 300001))
test_list.extend(second_list)


key = 29999
flag = False
start_time_naive = time.time()
for element in test_list:
    if element == key:
        flag = True
end_time_naive = time.time()
time_taken_naive = end_time_naive - start_time_naive

print(f"Naive element Exist? {flag}\n Time taken: {time_taken_naive}")

flag = False
start_time_in = time.time()
if key in test_list:
    flag = True
else:
    flag = False

end_time_in = time.time()
time_taken_in = end_time_in - start_time_in

print(f"IN method element Exist? {flag}\n Time taken: {time_taken_in}")


flag = False
start_time_in_set = time.time()
if key in set(test_list):
    flag = True
else:
    flag = False

end_time_in_set = time.time()
time_taken_in_set = end_time_in_set - start_time_in_set

print(f"IN set method element Exist? {flag}\n Time taken: {time_taken_in_set}")
