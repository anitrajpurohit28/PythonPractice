# ---- Creating a Dictionary ----

# empty dictionary
my_dict1 = {}
print(f"Empty Dictionary: {my_dict1}")

# with dict method
my_dict = dict({1: "geeks", 2: "for", 3: "geeks"})
print(my_dict)

# with list of pairs
my_dict2 = dict([(1, "geeks"), (2, "for"), (3, "geeks")])
print(my_dict2)


# nested dictionary
my_dict3 = {1: "geeks", 2: "For",
            3: {'A': "welcome", 'B': "to", 'C': "geeks"}}
print(my_dict3)


# --- adding elements----

# using assignment, one at a time
my_dict4 = dict() # or {}
my_dict4[0] = "geeks"
my_dict4[1] = "for"
my_dict4[2] = 1
print(my_dict4)

# adding set of values
my_dict4['value set'] = 2, 3, 4
print(my_dict4)

# update one of the value
my_dict4[2] = "welcome"
print(my_dict4)

# Adding nested key-value to dictionary
my_dict4[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print(my_dict4)


# ------- Accessing elements of dictionary -----
my_dict1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(my_dict1[2])
print(my_dict1.get(3,  "No such key"))
print(my_dict1.get(45, "No such key"))


# Accessing elements of Nested dictionary

my_dict2 = {'dict1': {1: 'geeks'},
            'dict2': {'Name': 'For'}}
print(my_dict2)
print(my_dict2['dict1'])
print(my_dict2['dict2']['Name'])

# ------- Removing elements from Dictionary -------

# Initial Dictionary
my_dict = {5: 'Welcome', 6: 'To', 7: 'Geeks',
           'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'},
           'B': {1: 'Geeks', 2: 'Life'}}
print(f"Initial Dictionary: \n{my_dict}")

del my_dict['B']
print(f"After deleting B: \n{my_dict}")

del my_dict['A'][3]
print(f"After deleting A[3]: \n{my_dict}")

popped = my_dict.pop('A')
print(f"After popping: {popped} \n{my_dict}")

# second arg: If item to be popped is not present, return second arg
popped = my_dict.pop('not_present', "Item Not Found")
print(f"Trying to pop 'not_present\nPopped item is: {popped}")

# popitem will delete last inserted element
popped = my_dict.popitem()
print(f"Popped {popped} with popitem.\n{my_dict}")

my_dict.clear()
print(f"Dictionary after calling clear: {my_dict}")

print("=====popitem=====")
# popitem
my_dict = {5: 'Welcome', 6: 'To', 7: 'Geeks', 'A': {1: 'Geeks', 2: 'For', 3: 'Geeks'}, 'B': {1: 'Geeks', 2: 'Life'}}
my_dict[1] = 'first'
print(my_dict)
print("Popped:")
while my_dict:
    popped = my_dict.popitem()
    print(popped)

# numerical values
dictionary = {"raj": 2, "striver": 3, "vikram": 4, "geeks": 5, "for": 5, "Geeks": 5, "for": 6}
print(f"Dictionary: {dictionary}")
print(f"Dict values: {dictionary.values()}")
print(f"Dict keys: {dictionary.keys()}")

# string values
dictionary = {}
print(dictionary.values())

# fromkeys, default "None" values is assigned
seq = {'a', 'b', 'c', 'd', 'e'}
res_dict = dict.fromkeys(seq)
print(f"fromkeys, no value: ", res_dict)

# from keys with value passed
res_dict = dict.fromkeys(seq, 123)
print(f"fromkeys, 123 passed: ", res_dict)

# fromkeys with list passed
temp_list = [7, 8, 9]

# this will lead to a shallow copy
res_dict = dict.fromkeys(seq, temp_list)
print(f"fromkeys, list {temp_list} passed:", res_dict)

# fromkeys, when list is modified, dict gets modified.
temp_list.append(10)
print(f"fromkeys, list modified:", res_dict)


print("----fromkeys, deepcopy-----")
# For deepcopy, follow this method
# fromkeys with list passed
temp_list = [7, 8, 9]
print("list: ", temp_list)
# this will lead to a shallow copy
res_dict = dict.fromkeys(seq, list(temp_list))
print(f"fromkeys, list {temp_list} passed:", res_dict)

# fromkeys, when list is modified, dict gets modified.
temp_list.append(10)
print("modified list: ", temp_list)
print(f"fromkeys, list modified:", res_dict)


# merge two dictionaries
print("---Merge two dictionaries---")
dict1 = {1: "geeks", 2: "for", 3: "geeks"}
dict2 = {"raj": 2, "striver": 3, "vikram": 4, "geeks": 5, "for": 5, "Geeks": 5, "for": 6}
print("dict 1: ", dict1)
print("dict 2: ", dict2)

dict3 = {**dict1, **dict2}
print("dict 3: ", dict3)

dict1.update(dict2)
print("after merge dict 2: ", dict3)

