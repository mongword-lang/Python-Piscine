#!/opt/pyenv/shims/python

import re, sys

if len(sys.argv) - 1 != 2:
    print("none")
else:
   matches = re.findall(re.escape(sys.argv[1]), sys.argv[2])
   if not matches:
       print("none")
   else:
      print(len(matches))
