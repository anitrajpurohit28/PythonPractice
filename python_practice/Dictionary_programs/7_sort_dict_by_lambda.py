# 7 Ways to sort list of dictionaries by values in Python – Using lambda function


list1 =[{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]
print(list1)

# sort only by age
print(sorted(list1, key=lambda i: i['age']))

# sort by age followed by name
print(sorted(list1, key=lambda i: (i['age'], i['name'])))

# reverse sort
print(sorted(list1, key=lambda i: (i['age'], i['name']), reverse=True))


