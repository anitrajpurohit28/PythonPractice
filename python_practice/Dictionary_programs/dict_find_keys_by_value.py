dictOfWords = {"hello": 56, "at": 23, "test": 43,
               "this": 97, "here": 43, "now": 97}
print(dictOfWords)


def get_key_by_value_naive(input_dict, value):
    print("get_key_by_value_naive")
    list_of_keys = []
    for item in input_dict.items():
        if item[1] == value:
            # put all the keys in list first
            list_of_keys.append(item[0])
    # return the list once all the keys are appended to list
    return list_of_keys


def get_key_list_by_value_list_naive(input_dict, value_list):
    # Input is value list
    print("get_key_list_by_value_list_naive")
    list_of_keys = []
    for item in input_dict.items():
        if item[1] in value_list:
            # put all the keys in list first
            list_of_keys.append(item[0])
    # return the list once all the keys are appended to list
    return list_of_keys


def get_keys_list_by_value_comprehension(input_dict, value):
    print("get_keys_list_by_value_comprehension")
    key_list = [k for k, v in input_dict.items() if v == value]
    return key_list


def get_keys_list_by_value_list_comprehension(input_dict, value_list):
    print("get_keys_list_by_value_list_comprehension")
    key_list = [k for k, v in input_dict.items() if v in value_list]
    return key_list


keys = get_key_by_value_naive(dictOfWords, 43)
print("naive: ", keys)

keys = get_keys_list_by_value_comprehension(dictOfWords, 43)
print("list comprehension: ", keys)

value_list = [43, 97]
key_list = get_key_list_by_value_list_naive(dictOfWords, value_list)
print(f"passed values: {value_list}\n"
      f"key_list: {key_list}")

value_list = [43, 97]
key_list = get_key_list_by_value_list_naive(dictOfWords, value_list)
print(f"passed values: {value_list}\n"
      f"key_list: {key_list}")

