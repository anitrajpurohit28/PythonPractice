# 2 Handling missing keys in Python dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)

# direct access; Leads to KeyError if key not present
print(dict1['a'])
# print(dict1['d']) # KeyError: 'd'

# get method, doesn't lead to key error.
# it either returns "None" or custom message passed.
print(dict1.get('a'))
print(dict1.get('d'))  # returns None
print(dict1.get('d', "my custom message"))

# setdefault: if the value is present, return the value
# else, insert the value passed
print(dict1.setdefault('a', 'xyz'))
print(dict1.setdefault('d', 'xyz'))
print(dict1)


# collections.defaultdict: dictionary constructed with this will always pass
# INFO what was set in the function "defaultdict", if failed.
print("--- default dict, lambda --- ")
import collections
def_dict = collections.defaultdict(lambda: "key_not_found default-dict")
def_dict[1] = 'a'
def_dict[2] = 'b'
def_dict[3] = 'c'
print(def_dict)

print(def_dict[1])
print(def_dict[4])

print("--- default dict, custom message --- ")
def custom_message():
    return "key_not_found custom message"
def_dict2 = collections.defaultdict(custom_message)
def_dict2[1] = 'a'
def_dict2[2] = 'b'
def_dict2[3] = 'c'
print(def_dict2)
print(def_dict2[1])
print(def_dict2[4])

