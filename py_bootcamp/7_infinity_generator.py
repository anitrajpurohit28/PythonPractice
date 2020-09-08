# Generates 1 2 3 4 1 2 3 4 ....

def current_beat_list():
    high = 100
    nums = [1, 2, 3, 4]
    i = 0
    result = []
    while len(result) < high:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

print(current_beat_list())


def current_beat_generator():
    nums = [1, 2, 3, 4]
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1
# call From python terminal
# counter = current_beat_generator()
# next(counter)
# for i in range(100):
#     next(counter)


