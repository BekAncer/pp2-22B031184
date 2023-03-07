s=input()
low,upp=0,0
for i in s:
    if i>=chr(65) and i<=chr(121):
        if(i==i.upper()):
            upp+=1
        elif(i==i.lower()):
            low+=1
print(low,upp)