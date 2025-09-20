import sys
import heapq
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

danger = [float("inf")] * (n + 1)
danger[1] = 0
pq = [(0, 1)]

while pq:
    cur_d, u = heapq.heappop(pq)
    if cur_d > danger[u]:
        continue
    for v, w in graph[u]:
        nd = max(cur_d, w)
        if nd < danger[v]:
            danger[v] = nd
            heapq.heappush(pq, (nd, v))

res = []
for i in range(1, n + 1):
    res.append(str(danger[i] if danger[i] != float("inf") else -1))
print(" ".join(res))
