import shelve

fruit = shelve.open("shelf_test_file")
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["orange"])
print(fruit["lemon"])
fruit["lime"] = "great with tequila"

print(fruit)
for snack in fruit:
    print(snack + ": " + fruit[snack])

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        print(fruit[dict_key])
    else:
        print("We don't have a ", dict_key)


ordered_keys = list(fruit.keys())
ordered_keys.sort()
print("-"*20)

for f in ordered_keys:
    print("{} - {}".format(f, fruit[f]))

fruit.close()






# # Can't fetch values from closed shelves!
# with shelve.open("shelf_test_file") as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
# print(fruit["orange"])
# print(fruit)



# # Can fetch values here as its assigned using dictionary!!!
# don't know why!
# with shelve.open("shelf_test_file") as fruit:
#     fruit = {'orange': "a sweet, orange, citrus fruit",
#              'apple':  "good for making cider",
#              'lemon':  "a sour, yellow citrus fruit",
#              'grape':  "a small, sweet fruit growing in bunches",
#              'lime' :  "a sour, green citrus fruit"}
#
# print(fruit["orange"])
# print(fruit)


