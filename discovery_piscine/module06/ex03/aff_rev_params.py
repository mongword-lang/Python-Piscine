#!/opt/pyenv/shims/python

import sys

if len(sys.argv) -1 < 2:
    print("none")
else:
    print("\n".join(reversed(sys.argv[1:])))
