def dijistra(G,s,t,N=None):
    unvisited ={i:None for i in N}
    visited = {}
    current = s
    currentdis = 0
    unvisited[current] = currentdis
    while True:
        for neighb,dis in G[current].items():
            if neighb not in unvisited:continue
            newdis = currentdis + dis
            if unvisited[neighb] is None or unvisited[neighb] > newdis:
                unvisited[neighb] = newdis
        visited[current] = currentdis
        del unvisited[current]
        if not unvisited: break
        candidates = [n for n in unvisited.items() if n[1]]#这句判断的是找出距离不为0的点作为候选点
        current, currentdis = sorted(candidates,key=lambda x:x[1])[0]#这句利用python的高级排序sorted用map的第二值作为排序的key
    return visited[t]

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
G  = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

print(dijistra(G,'A','G',nodes))
