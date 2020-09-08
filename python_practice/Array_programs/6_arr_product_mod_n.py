# 6. Python Program for Find reminder of array multiplication divided by n

arr = [100, 10, 5, 25, 35, 14, 2, 32, 14, 32, 64, 31]
mod_val = 11

def arr_prod_mod(arr, mod_val):
    res = arr[0]
    length = len(arr)
    for i in range(length):
        res = (res*arr[i]) % mod_val
    print("Result:", res)

arr_prod_mod(arr, mod_val)