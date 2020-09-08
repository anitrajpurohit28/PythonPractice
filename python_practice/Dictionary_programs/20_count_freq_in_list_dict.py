# 20 Counting the frequencies in a list using dictionary in Python

input_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

def freq_count_iter(input_list):
    print("freq_count_iter")
    freq = {}
    for i in input_list:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1
    for k, v in freq.items():
        print(f"{k} -> {v}")

def freq_count_count_method(input_list):
    print("freq_count_count_method")
    freq = {}
    for item in input_list:
        if item in freq.keys():
            # since we are using count method, it'll return the
            # same result, thus, pass
            pass
        else:
            freq[item] = input_list.count(item)
    for k, v in freq.items():
        print(f"{k} -> {v}")

def freq_count_dict(input_list):
    print("freq_count_dict")
    freq = {}
    for item in input_list:
        freq[item] = freq.get(item, 0) + 1
    for k, v in freq.items():
        print(f"{k} -> {v}")

freq_count_iter(input_list)
freq_count_count_method(input_list)
freq_count_dict(input_list)

