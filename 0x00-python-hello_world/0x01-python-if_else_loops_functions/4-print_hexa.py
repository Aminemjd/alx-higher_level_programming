#!/usr/bin/python3
for i in range(0, 99):
    print("{0} = {1}".format(i, hex(i)))






5-print_comb2.py


#!/usr/bin/python3
for i in range(99):
    print("{:02d}".format(i), end=", ")
print("{:02d}".format(99))

