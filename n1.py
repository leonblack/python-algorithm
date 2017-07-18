def merg_sort(seq):
    mid = len(seq)//2
    lft,rgt=seq[:mid],seq[mid:]
    if(len(lft) > 1):lft=merg_sort(lft)
    if(len(rgt) > 1):rgt=merg_sort(rgt)
    res=[]
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    print(lft,rgt,res,(lft or rgt) + res)
    return (lft or rgt ) + res

p = [1 ,3,8,2,5,0]
merg_sort(p)