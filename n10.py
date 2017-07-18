def walk(G,s,S=set()):
    P,Q = dict(),set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u

    return P

def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:continue
        C = walk(G,u)
        seen.update(C)
        comp.append(C)
    return comp


G = {
    0: set([1, 2]),
    1: set([0, 2]),
    2: set([0, 1]),
    3: set([4, 5]),
    4: set([3, 5]),
    5: set([3, 4])
}

print([list(sorted(C)) for C in components(G)])