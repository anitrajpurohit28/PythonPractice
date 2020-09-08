# Finding keys from values in Dict

# creating a new dictionary
my_dict = {"java": 100, "python": 112, "c programming": 110}
counter = {'e': 4, 'g': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}


def get_key_from_dict_by_list_index(dict, val):
    # converting the keys and values to list
    # so that we can run index method later
    key_list = list(dict.keys())
    value_list = list(dict.values())

    print(key_list[value_list.index(val)])


# function to return key for any value
def get_key_from_dict_iter_items(dict, val):
    for key, value in dict.items():
        if val == value:
            print(key)
    return "key doesn't exist"


get_key_from_dict_by_list_index(my_dict, 110)
get_key_from_dict_by_list_index(counter, 4)

get_key_from_dict_iter_items(my_dict, 110)
get_key_from_dict_iter_items(counter, 4)
