# 5 Python | Ways to remove a key from dictionary

print("--- del dict[index] ---")
test_dict = {1: 100, 2: 200, 3: 300, 4: 400}
print("Before delete test_dict[2] :", test_dict)
del test_dict[2]
print("After delete test_dict[2] :", test_dict)
# del test_dict[5]  # this will lead to KeyError: as key is not found

print("--- dict.pop() ---")
# this will not give the key error
test_dict = {1: 100, 2: 200, 3: 300, 4: 400}
print("Before popping key 2 :", test_dict)
popped = test_dict.pop(2)
print("Item popped: ", popped)
print("After popping key 2 :", test_dict)
popped = test_dict.pop(10, "key not found")
print("Item popped: ", popped)
print("After popping non-existing key 10 :", test_dict)

print("---dict.items() + dict comprehension ---")
test_dict = {1: 100, 2: 200, 3: 300, 4: 400}
key_to_remove = 2
print(f"Before removing key={key_to_remove}:", test_dict)
new_dict = {key: value for key, value in test_dict.items() if key != key_to_remove}
print(f"After removing key={key_to_remove}:", new_dict)
