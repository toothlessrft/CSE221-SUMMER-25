from collections import defaultdict, deque
import sys
n, m, s, d = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))

graph = defaultdict(list)
for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

for key in graph:
    graph[key].sort()

def bfs(s, d, n):
    q = deque([s])
    dist = [float('inf')] * (n + 1)
    par = [-1] * (n + 1)
    dist[s] = 0

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                par[neighbor] = node
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    if dist[d] == float('inf'):
        return None

    path = []
    current = d
    while current != -1:
        path.append(current)
        current = par[current]
    path.reverse()
    return dist[d], path

result = bfs(s, d, n)
if result is None:
    print(-1)
else:
    length, path = result
    print(length)
    print(" ".join(map(str, path)))
