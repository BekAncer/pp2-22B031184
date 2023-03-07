e=(False,True,False)

def TrueTuple(l):
    cnt=0
    k=0
    for i in l:
        k=k+1
        if i:
            cnt=cnt+1
    if cnt==k:
        return True
    else:
        return False
print(TrueTuple(e))