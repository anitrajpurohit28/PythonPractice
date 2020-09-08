# get dimensions n, m
# dimension of A and B are "m"
# length of A is "n"

n, m = map(int, input().split())
#print(n, m)

input_list = list(map(int, input().split()))
#print(input_list)

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

happiness_index = 0

for i in input_list:
    if i in set_a:
        happiness_index += 1
    elif i in set_b:
        happiness_index -= 1
    else:
        pass

print(happiness_index)