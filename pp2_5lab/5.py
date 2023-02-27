# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re 
s = input() 
pattern = r'a+.+b$' 
ls = re.findall(pattern, s) 
print(*ls)