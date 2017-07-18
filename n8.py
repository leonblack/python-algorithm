from random import randrange
def celeb(G):
    n = len(G)
    u,v = 0,1
    for c in range(2,n+1):
        if G[u][v]:u = c
        else: v = c
    if u==n: c = v
    else: c = u
