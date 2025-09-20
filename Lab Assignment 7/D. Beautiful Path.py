import sys
import heapq
from collections import defaultdict
n, m, s, d = map(int, sys.stdin.readline().split())
weights = [0] + list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

dist = [float("inf")] * (n + 1)
dist[s] = weights[s]
pq = [(weights[s], s)]

while pq:
    cost, u = heapq.heappop(pq)
    if cost > dist[u]:
        continue
    for v in graph[u]:
        new_cost = cost + weights[v]
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(pq, (new_cost, v))

print(-1 if dist[d] == float("inf") else dist[d])
