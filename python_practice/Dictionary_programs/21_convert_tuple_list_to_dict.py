# 21 Python | Convert a list of Tuples into Dictionary
"""
Input : [("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
Output : {'akash': [10], 'gaurav': [12], 'anand': [14],
          'ashish': [30], 'akhil': [25], 'suraj': [20]}

Input : [('A', 1), ('B', 2), ('C', 3)]
Output : {'B': [2], 'A': [1], 'C': [3]}

Input : [("Nakul",93), ("Shivansh",45), ("Samved",65),
             ("Yash",88), ("Vidit",70), ("Pradeep",52)]
Output : {'Nakul': [93], 'Shivansh': [45], 'Samved': [65],
            'Yash': [88], 'Vidit': [70], 'Pradeep': [52]}

Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
"""

input_list1 = [("akash", 10), ("gaurav", 12), ("anand", 14),
               ("suraj", 20), ("akhil", 25), ("ashish", 30)]

input_list2 = [('A', 1), ('B', 2), ('C', 3)]
input_list3 = [("Nakul", 93), ("Shivansh", 45), ("Samved", 65),
               ("Yash", 88), ("Vidit", 70), ("Pradeep", 52)]

input_list4 = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]

def convert_tuple_list_to_dict_subscript(input_list):
    output_dict = {}
    for item in input_list:
        output_dict[item[0]] = item[1]
    print(output_dict)

def convert_tuple_list_to_dict_setdefault(input_list):
    output_dict = {}
    for a, b in input_list:
        # setdefault will return second arg if key not found
        # in this case, an empty list. We'll append b in the list then
        # if key is present, it'll return the key, we'll append b to it
        output_dict.setdefault(a, []).append(b)
    print(output_dict)

def convert_tuple_list_to_dict_dict_constructor(input_list):
    output_dict = dict(input_list)
    print(output_dict)

print(dict(input_list1))
convert_tuple_list_to_dict_subscript(input_list1)
convert_tuple_list_to_dict_dict_constructor(input_list1)
convert_tuple_list_to_dict_setdefault(input_list1)

print(dict(input_list2))
convert_tuple_list_to_dict_subscript(input_list2)
convert_tuple_list_to_dict_dict_constructor(input_list2)
convert_tuple_list_to_dict_setdefault(input_list2)

print(dict(input_list3))
convert_tuple_list_to_dict_subscript(input_list3)
convert_tuple_list_to_dict_dict_constructor(input_list3)
convert_tuple_list_to_dict_setdefault(input_list3)

print(dict(input_list4))
convert_tuple_list_to_dict_subscript(input_list4)
convert_tuple_list_to_dict_dict_constructor(input_list4)
convert_tuple_list_to_dict_setdefault(input_list4)

