# 2. Python Program to find largest element in an array

arr = [5, 11, 33, 34, 45, 15, 10]
def find_largest_1(arr):
    large = arr[0]
    for item in arr:
        if item > large:
            large = item
    return large


print(find_largest_1(arr))
print(max(arr))
