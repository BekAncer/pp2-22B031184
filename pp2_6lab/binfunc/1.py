import math
l=list(map(int,input().split()))
#print(math.prod(list))
cnt=1
for i in l:
    cnt=cnt*i
print(cnt)