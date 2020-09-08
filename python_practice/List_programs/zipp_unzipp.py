alpha_list = ['A', 'B', 'C', 'D', 'E']
edibles_list = ["apple", "banana", "carrot", "drumstick", "Endive"]
merge_dict = {}
merge_list = []

# zipping
for alpha, edible in zip(alpha_list, edibles_list):
    merge_dict[alpha] = edible
    merge_list.append(f"{alpha}: {edible}")

print(merge_dict)
print(merge_list)
print(list(merge_dict.items()))
# un-zipping


a_tuple, e_tuple = zip(*merge_dict.items())
print("a_list: ", a_tuple)
print("e_list: ", e_tuple)




