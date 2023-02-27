# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re 
 
s = input() 
pattern = r'[a-z]+_[a-z]+' 
 
ls = re.findall(pattern, s) 
print(*ls)