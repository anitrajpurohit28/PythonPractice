# Convert Dictionaries to list of tuples

# Making dictionary with with lists
alpha_list = ['A', 'B', 'C', 'D', 'E']
edibles_list = ["apple", "banana", "carrot", "drumstick", "Endive"]
merge_dict = {}

# zipping
for alpha, edible in zip(alpha_list, edibles_list):
    merge_dict[alpha] = edible

print("Dictionary: ", merge_dict)

print("---using list.items()----")
# merge_dict.items() will return dict object
# dict_items([('A', 'apple'), ('B', 'banana'), ('C', 'carrot'), ('D', 'drumstick'), ('E', 'Endive')])
list1 = list(merge_dict.items())
print(list1)

print("---List comprehension----")
list2 = [(k, v) for k, v in merge_dict.items()]
print(list2)

print("---Zip-----")
list3 = list(zip(merge_dict.keys(), merge_dict.values()))
print(list3)

print("---Iteration for_in ---")
list4 = []
for k, v in merge_dict.items():
    list4.append((k, v))
print(list4)

print("---Iteration for_index ---")
list5 = []

for index in merge_dict:
    item = (index, merge_dict[index])
    list5.append(item)

print(list5)

print("--- collection----")
import collections
list_of_tuple = collections.namedtuple('List', 'alphabet food')
list6 = [list_of_tuple(*item) for item in merge_dict.items()]
print(list6)

"""
print("=====")
for item in merge_dict.items():
    print(item)
    print(*item)
"""
