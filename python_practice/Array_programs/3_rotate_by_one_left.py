# 3. Python Program for array rotation

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rotate_one_left(arr):
    temp = arr[0]
    for index in range(0, len(arr)-1):
        arr[index] = arr[index+1]
    arr[len(arr)-1] = temp


def rotate_array(arr, rotate_no):
    for i in range(rotate_no):
        rotate_one_left(arr)


print("Before rotation:", arr)
rotate_array(arr, 3)
print("After rotation: ", arr)


print("--- ---")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def juggling_algo(arr, rotation_no):
    division = gcd(len(arr), rotation_no)
    for i in range(division):
        temp = arr[i]
        j = arr[i]
        while j < len(arr):
            arr[j] = arr[j+division]
            j += division

    print(arr)


print("Before rotation:", arr)
juggling_algo(arr, 3)
print("After rotation: ", arr)

