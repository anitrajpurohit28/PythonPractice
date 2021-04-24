# check if any number if repeated in given two files
f1 = open("test1.log", 'r')
f2 = open("test2.log", 'r')

f1_lines = f1.readlines()
f2_lines = f2.readlines()

f1_list = []
f2_list = []

for line in f1_lines:
    f1_list.append(line.strip())

for line in f2_lines:
    f2_list.append(line.strip())

print(f1_list)
print(f2_list)

res = []
for line in f1_lines:
    if line in f2_lines:
        res.append(True)
    else:
        res.append(False)

print(res)
print(all(res))

f1.close()
f2.close()
