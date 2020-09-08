# 9 Python | Count occurrences of an element in a list

input_list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
key = 10

print("------- for loop-------")
count = 0
for element in input_list:
    if element == key:
        count += 1

print(f"Element {key} occurred {count} times")


print("-------builtin count()-------")
count = 0
count = input_list.count(key)

print(f"Element {key} occurred {count} times")

print("-------counter from collections-------")
import collections

counter_list = collections.Counter(input_list)
count = counter_list[key]
print(counter_list)
print(f"Element {key} occurred {count} times")

print("-------item counter--------")
# Let’s say we want to count each element in a list and store in another list or say dictionary.
lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

item_counter_list = [[item, lst.count(item)] for item in set(lst)]
print(item_counter_list)

item_counter_dict = [{item: lst.count(item)} for item in set(lst)]
print(item_counter_dict)
