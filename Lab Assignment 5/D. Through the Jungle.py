from collections import defaultdict, deque
import sys
n, m, s, d, k = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)

def bfs(s, d):
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

result1 = bfs(s, k)
result2 = bfs(k, d)
if result1 is None or result2 is None:
    print(-1)
else:
    length1, path1 = result1
    length2, path2 = result2
    print(length1 + length2)
    print(" ".join(map(str, path1 + path2[1:])))
