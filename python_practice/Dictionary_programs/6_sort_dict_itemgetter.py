# 6 Ways to sort list of dictionaries by values in Python – Using itemgetter

from operator import itemgetter

list1 =[{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]
print(list1)

# sort only by age
print(sorted(list1, key=itemgetter('age')))

# sort by age followed by name
print(sorted(list1, key=itemgetter('age', 'name')))

# reverse sort
print(sorted(list1, key=itemgetter('age', 'name'), reverse=True))



