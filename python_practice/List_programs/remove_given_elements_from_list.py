
list1 = [1, 2, 3, 4, 1, 2, 3, 1, 1, 4]
print(list1)
list1.remove(1)
print(list1)

# remove all 1's, using "count"
while list1.count(1):
    list1.remove(1)
print("---After removing all 1's----")
print(list1)
# remove all 2's, using "in"
while 2 in list1:
    list1.remove(2)
print("---After removing all 2's----")

print(list1)