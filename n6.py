def navie_max_permu(M,A=None):
    if A is None:
        A =set(range(len(M)))
    if len(A) == 1: return A
    B=set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return navie_max_permu(M,A)
    return A

M=[2,2,0,5,3,5,7,4]
print(navie_max_permu(M))
