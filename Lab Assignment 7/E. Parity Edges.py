import sys
import heapq
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
U = list(map(int, sys.stdin.readline().split()))
V = list(map(int, sys.stdin.readline().split()))
W = list(map(int, sys.stdin.readline().split()))

edges = defaultdict(list)
for i in range(m):
    edges[U[i] - 1].append((V[i] - 1, W[i]))

dist = [[float("inf")] * 2 for _ in range(n)]
pq = []

for nxt, wt in edges[0]:
    p = wt & 1
    dist[nxt][p] = wt
    heapq.heappush(pq, (wt, nxt, p))

while pq:
    cur_d, u, last_p = heapq.heappop(pq)
    if cur_d != dist[u][last_p]:
        continue
    for v, wt in edges[u]:
        np = wt & 1
        if np != last_p:
            nd = cur_d + wt
            if nd < dist[v][np]:
                dist[v][np] = nd
                heapq.heappush(pq, (nd, v, np))

res = min(dist[n - 1])
print(res if res < float("inf") else -1)
