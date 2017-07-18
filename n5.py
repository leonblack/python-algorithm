def sel_sort_rec(seq,i):
    if i == 0 : return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:max_j = j
    seq[i],seq[max_j] = seq[max_j],seq[i]
    sel_sort_rec(seq,i-1)

n=[1,23,455,6,2,4]
sel_sort_rec(n,5)
print(n)