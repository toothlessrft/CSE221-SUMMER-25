from collections import defaultdict, deque
import sys

n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    far_node, max_d = start, 0

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > max_d:
                    max_d, far_node = dist[v], v
    return far_node, max_d

a, _ = bfs(1)
b, length = bfs(a)

print(length)
print(a, b)
