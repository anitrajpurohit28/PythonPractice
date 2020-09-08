# 4 Python | Ways to find length of list
from operator import length_hint
import time
test_list = list(range(1, 300001))
# print(test_list)

# naive method
start_time_naive = time.time()
count = 0
for entry in test_list:
    count += 1
end_time_naive = time.time()
time_taken_naive = end_time_naive - start_time_naive
print(f"Naive method: {count}\ttime_taken: {time_taken_naive}")

start_time_len = time.time()
list_len = len(test_list)
end_time_len = time.time()
time_taken_len = end_time_len - start_time_len
print(f"len method: {count}\ttime_taken: {time_taken_len}")

start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = time.time()
time_taken_hint = end_time_hint - start_time_hint
print(f"hint method: {count}\ttime_taken: {time_taken_hint}")
