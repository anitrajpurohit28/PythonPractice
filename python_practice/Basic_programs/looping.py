
# C-style looping
# considered bad in python; Error prone
print("----C style-----")
cars = ['Aston', 'Audi', 'McLaren']
i = 0
while i < len(cars):
    print(cars[i])
    i += 1

print("----for in ----")
for car in cars:
    print(car)

print("----using range and len ----")
# accessing list with index
for i in range(len(cars)):
    print(cars[i])

# Enumerate
print("----using enumerate, 2 variables ----")
for i, car in enumerate(cars):
    print(i, car)

print("----using enumerate, 2 variables with start parameter ----")
for i, car in enumerate(cars, start=1):
    print(i, car)

print("----using enumerate, 1 variables, index ----")
for x in enumerate(cars):
    print(x[0], x[1])

print("-----list after enumeration----")
print(list(enumerate(cars)))

print("===== multiple iterators ====")
# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and its accessories
# First three items store prices of cars and
# next two items store prices of accessories.
prices = {1: "570000$", 2: "68000$", 3: "450000$",
          4: "8900$", 5: "4500$"}

for index, car in enumerate(cars, start=1):
    print(f"{index} Car: {car} price: {prices[index]}")

for index, accessory in enumerate(accessories, start=1):
    print(f"{index+len(cars)} Accessories: {accessory} price: {prices[index+len(cars)]}")

print("----Merging two lists into with enumerate----")
cars = ["Aston", "Audi", "McLaren", "GPS kit", "Car repair-tool kit"]
prices = ["570000$", "68000$", "450000$", "8900$", "4500$"]
dictionary = {}
for index, car in enumerate(cars):
    print(f"{car}: {prices[index]}")
    dictionary[car] = prices[index]

print(dictionary)
