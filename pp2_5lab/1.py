#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
 
s = input()

pattern = r'a(b?)'
res = re.search(pattern, s)

if res:
    print(res.group())
