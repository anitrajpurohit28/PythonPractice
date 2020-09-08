# 7. Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M

arr = [5, -1, -1, 1, 2, 3]
mod_val = 7

def reconstruct_arr(arr, mod):
    new_arr = []
    new_arr.append(arr[0])
    for i in range(1, len(arr)):
        new_arr.append((arr[i] + arr[i-1])

    print(new_arr)

reconstruct_arr(arr, mod_val)