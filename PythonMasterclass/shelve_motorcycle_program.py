import shelve

with shelve.open("bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["color"] = "red"
    # bike["engin_size"] = 250
    #
    # del bike["engin_size"]
    for key in bike:
        print(f"{key} -> {bike[key]}")

    print("=" * 40)

    print(bike["engine_size"])
    print(bike["color"])
