import sys
import heapq
from collections import defaultdict
n, m, s, d = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

shortest = [float("inf")] * (n + 1)
second_shortest = [float("inf")] * (n + 1)
shortest[s] = 0

heap = [(0, s)]

while heap:
    cost, node = heapq.heappop(heap)
    for nei, w in graph[node]:
        total = cost + w
        if total < shortest[nei]:
            second_shortest[nei] = shortest[nei]
            shortest[nei] = total
            heapq.heappush(heap, (total, nei))
        elif shortest[nei] < total < second_shortest[nei]:
            second_shortest[nei] = total
            heapq.heappush(heap, (total, nei))

res = second_shortest[d]
print(res if res != float("inf") else -1)
