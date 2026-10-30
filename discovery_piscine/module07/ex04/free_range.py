#!/opt/pyenv/shims/python

import sys

if len(sys.argv) != 3:
    print("none")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if a >= b:
       print("none")
    else:
        print(list(range(a, b + 1)))

