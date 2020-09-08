input_dict = {'john': 4, 'johnny': 4, 'jamie': 3, 'jackie': 2}
output_dict = {}
for value in input_dict.values():
    output_dict[value] = []

for key, value in input_dict.items():
    output_dict[value].append(key)

print("Input: ", input_dict)
print("Output: ", output_dict)
print(" ----append all keys as list of values------- ")
input_dict = {'john': 4, 'johnny': 4, 'jamie': 3, 'jackie': 2}
output_dict = {}

for key, value in input_dict.items():
    if value in output_dict.keys():
        output_dict[value].append(key)
    else:
        output_dict[value] = []
        output_dict[value].append(key)

print("Input: ", input_dict)
print("Output: ", output_dict)


print(" ----only multiple same values in list------- ")
input_dict = {'john': 4, 'johnny': 4, 'jamie': 3, 'jackie': 2}
output_dict = {}

for key, value in input_dict.items():
    if output_dict.get(value, "none") is not "none":
        current_value = output_dict[value]
        output_dict[value] = []
        output_dict[value].append(current_value)
        output_dict[value].append(key)
    else:
        output_dict[value] = key

print("Input: ", input_dict)
print("Output: ", output_dict)
