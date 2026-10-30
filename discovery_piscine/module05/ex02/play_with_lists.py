#!/usr/bin/env python3

original= [2,8,9,48,8,22,-12,2]
modified= []

for num in original :
    if num >5:
        modified.append(num + 2)

print("Original list:", original)
print("Modified list:", modified)
