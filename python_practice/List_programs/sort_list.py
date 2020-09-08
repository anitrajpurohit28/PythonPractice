numbers = [1, 3, 4, 5, 2, 5]
numbers.sort()
print(numbers)

decimal_numbers = [1.223, 3.42, 1.112, 2.44]
decimal_numbers.sort(reverse=True)
print(decimal_numbers)

words = ['geeks', 'for', 'geeks']
words.sort()
print(words)

print("-----custom sort------")
def sort_second(val):
    return val[1]

list1 = [(1, 2), (4, 7), (3, 1), (1, 3)]
list1.sort()
print(list1)

# sorted based on second value of tuple
list2 = [(1, 2), (4, 7), (3, 1), (1, 3)]
list2.sort(key=sort_second)
print(list2)
