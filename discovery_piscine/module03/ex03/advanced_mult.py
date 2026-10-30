#!/usr/bin/env python3

num = 0
while num <= 10:
    i = 0
    row = ""
    while i <= 10:
        row += str(num *i) + " "
        i +=1
    print(f"Table of {num}: {row.rstrip()}")
    num += 1    

