# check if list are equal

print("------ sort and == ---------")
test_list1 = list(range(1, 11))
test_list2 = list(range(10, 0, -1))
print(test_list1)
print(test_list2)

test_list1.sort()
test_list2.sort()

if test_list1 == test_list2:
    print("Lists are equal")
else:
    print("Lists are not equal")

print("------ collections.counter ---------")
import collections

test_list1 = list(range(1, 11))
test_list2 = list(range(10, 0, -1))

list_count1 = collections.Counter(test_list1)
list_count2 = collections.Counter(test_list2)

if list_count1 == list_count2:
    print("Lists are equal")
else:
    print("Lists are not equal")