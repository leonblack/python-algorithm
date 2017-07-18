def ins_sort_rec(seq,i):
    if i==0:return
    ins_sort_rec(seq,i-1)
    j=i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j],seq[j-1]
        j-=1


n = [1,2,4,2,3,5,73,1]
ins_sort_rec(n,len(n)-1)
print(n)