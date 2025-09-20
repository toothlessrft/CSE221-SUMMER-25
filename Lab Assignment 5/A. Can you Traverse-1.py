from queue import Queue
from collections import defaultdict
import sys

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(g, s):
    q = Queue()
    visited = [False] * (n + 1)
    visited[s] = True
    q.put(s)
    res = []

    while not q.empty():
        node = q.get()
        res.append(node)
        for neighbor in sorted(g[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                q.put(neighbor)
    return res

src = 1
result = bfs(graph, src)
print(" ".join(map(str, result)))
