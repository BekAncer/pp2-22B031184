# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re 
 
s = input() 
pattern = r'ab{2,3}?' 
res = re.search(pattern, s) 
 
if res: 
    print(res.group())