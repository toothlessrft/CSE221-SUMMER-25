import sys
import heapq
from collections import defaultdict

n, m, s, t = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

da = dijkstra(s)
db = dijkstra(t)

best, node = float("inf"), -1
for i in range(1, n + 1):
    if da[i] != float("inf") and db[i] != float("inf"):
        cur = max(da[i], db[i])
        if cur < best or (cur == best and i < node):
            best, node = cur, i

if node == -1:
    print(-1)
else:
    print(best, node)
