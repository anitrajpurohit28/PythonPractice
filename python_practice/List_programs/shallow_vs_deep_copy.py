# shallow copy
# Changes made to copied list does reflect on original list

import copy

list1 = [1, 2, [3, 5], 4]
# shallow copy methods
list2 = list1.copy()
list3 = copy.copy(list1)
list4 = list1[:]
list5 = list1
print("----Shallow copy; Before modify----")
print("list2 list.copy: ", list2)
print("list3 copy.copy: ", list3)
print("list4 list[:]:   ", list4)
print("Original list:   ", list1)
list2.append(5)
list3.append(6)
list4.append(7)
list5.append(8)
# modify the list using list2
list2[2][0] = 7
print("----Shallow copy; After modify----")
print("list2 list.copy: ", list2)
print("list3 copy.copy: ", list3)
print("list4 list[:]:   ", list4)
print("Original list:   ", list1)

# Deep copy
# Changes made to copied list does NOT reflect on original list

# Deep copy methods
list6 = copy.deepcopy(list1)
print("----Deep copy; Before modify----")
print("list6 copy.deepcopy: ", list6)
print("Original list:       ", list1)
list6.append(9)

# modify both original list and the deep copied list
list1[2][0] = 9
list6[2][0] = 1

print("----Deep copy; After modify----")
print("list6 copy.deepcopy: ", list6)
print("Original list:       ", list1)
