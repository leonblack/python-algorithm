def ins_sort(seq):
    for i in range(1,len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1],seq[j] = seq[j],seq[j-1]
            j-=1

n = [12,4,2,3,6]
ins_sort(n)
print(n)