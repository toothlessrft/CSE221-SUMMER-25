import sys
import heapq
from collections import defaultdict
n, m, s, d = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
w = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for i in range(m):
    graph[u[i]].append((v[i], w[i]))

def dijkstra(start, end):
    dist = [float("inf")] * (n + 1)
    parent = [-1] * (n + 1) 
    dist[start] = 0

    pq = [(0, start)] 
    visited = [False] * (n + 1)

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True

        for nei, wt in graph[node]:
            if dist[nei] > cur_dist + wt:
                dist[nei] = cur_dist + wt
                parent[nei] = node
                heapq.heappush(pq, (dist[nei], nei))

    if dist[end] == float("inf"):
        return -1, []
    
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return dist[end], path

ans, path = dijkstra(s, d)
if ans == -1:
    print(-1)
else:
    print(ans)
    print(" ".join(map(str, path)))
