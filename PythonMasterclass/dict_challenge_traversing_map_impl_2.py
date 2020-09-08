locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0, "2": 2, "3": 3, "4": 4, "5": 5},
         2: {"N": 5, "Q": 0, "5": 5},
         3: {"W": 1, "Q": 0, "1": 1},
         4: {"N": 1, "W": 2, "Q": 0, "1": 1, "2": 2},
         5: {"S": 1, "W": 2, "Q": 0, "1": 1, "2": 2}}

vocabulary = {"QUIT": "Q",
              "EAST": "E",
              "WEST": "W",
              "NORTH": "N",
              "SOUTH": "S",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"
              }

loc = 1
print(locations[loc])
while True:
    if loc == 0:
        break

    available_exits = ", ".join(exits[loc].keys())
    direction = input("Available Location " + available_exits + ": ").upper()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
    print(locations[loc])

















# loc = 1
# while True:
#
#     if loc == 0:
#         break
#     print(locations[loc])
#
#     available_exits = ", ".join(exits[loc])
#     direction = input("Availabe exits are " + available_exits + ": ")
#
#     if direction in available_exits:
#         loc = exits[loc][direction]
#         print(locations[loc])
#     else:
#         print("You cannot go there")

