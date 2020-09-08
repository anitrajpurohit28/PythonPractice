# jabber = open("sample.txt")
# print(jabber)
# for line in jabber:
#     # if "jabber" in line.lower():
#     #     print(line, end='')
#     print(line, end='')
# jabber.close()

# with open("sample.txt") as jabber:
#     for line in jabber:
#         if "jabber" in line.lower():
#             print(line, end='')
#         #print(line, end='')
#

# "readline" will read one line at a time
# good method when we have too many lines to read
# efficient memory wise

# with open("sample.txt") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()


# # "readlines" will read all lines at once, linewise
# with open("sample.txt") as jabber:
#     lines = jabber.readlines()
#     #print(lines)
#     for line in lines:
#         print(line, end='')
#         line = jabber.readline()

# "read" will read all the characters as one stream, at once
# with open("sample.txt") as jabber:
#     lines = jabber.read()
# for line in lines:
#     print(line, end='')

# print(lines[::-1])

# with open("sample.txt") as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')

