# Write a Python program to split a string at uppercase letters.
import re
txt = input()
pattern = r'[A-Z][^A-Z]*'
print(*re.findall(pattern ,txt))