# Write a Python program to convert a given camel case string to snake case.
import re 
pattern = r'(.+?)([A-Z])'
def snake(match): 
    return match.group(1).lower() + "_" + match.group(2).lower() 
words = input() 
results = re.sub(pattern, snake, words) 
print(results)
