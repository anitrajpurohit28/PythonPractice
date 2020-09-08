# 6 Different ways to clear a list in Python

list1 = list(range(1, 20))
print(f"Before clear: {list1}")
list1.clear()
print(f"After clear: {list1}")

list1 = list(range(1, 20))
print(f"Before clear: {list1}")
list1 = []
print(f"After clear: {list1}")


list1 = list(range(1, 20))
print(f"Before clear: {list1}")
list1 *= 0
print(f"After clear: {list1}")


list1 = list(range(1, 20))
print(f"Before clear: {list1}")
del list1[:]
print(f"After clear: {list1}")
