#!/opt/pyenv/shims/python

import sys

if len(sys.argv) - 1 == 0:
    print("none")
else: 
   for arg in sys.argv[1:]:
     if arg.find("ism") != len(arg) -3:
        print(arg + "ism")

