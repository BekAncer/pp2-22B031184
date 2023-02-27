# Write a Python program to insert spaces between words starting with capital letters.
import re 
text = input() 
pattern = '[A-Z][a-z]*' 
l = re.split('(?=[A-Z])', text)
# res = re.findall(pattern, text) 
print(*l)
