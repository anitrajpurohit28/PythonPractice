# 8 Python | Merging two Dictionaries

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {7: 'x', 8: 'y', 3: 'z'}

dict1.update(dict2)

print(f"Merged Dict: {dict1}")

dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {7: 'x', 8: 'y', 3: 'z'}

merged_dict = {**dict1, **dict2}
print(f"Merged Dict: {merged_dict}")
