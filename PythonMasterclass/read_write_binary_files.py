# with open("binary", "bw") as bin_file:
#     bin_file.write(bytes(range(16)))
#
# with open("binary", "br") as bin_file:
#     for b in bin_file:
#         print(b)

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E
y = 2998302     # 02 2D C0 1E

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(y.to_bytes(4, 'little'))

with open("binary2", "br") as bin_file:
    a_read = int.from_bytes(bin_file.read(2), "big")
    print(a_read)
    b_read = int.from_bytes(bin_file.read(2), "big")
    print(b_read)
    c_read = int.from_bytes(bin_file.read(4), "big")
    print(c_read)
    x_read = int.from_bytes(bin_file.read(4), "big")
    print(x_read)
    y_read = int.from_bytes(bin_file.read(4), "little")
    print(y_read)

