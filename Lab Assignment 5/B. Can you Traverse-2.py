from collections import defaultdict
import sys

n, m = map(int, sys.stdin.readline().split())
u = list(map(int, sys.stdin.readline().split()))
v = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

def dfs(graph, src):
    visited = set()
    stack = [src]
    res = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            res.append(node)
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)

    return res

src = 1
result = dfs(graph, src)
print(" ".join(map(str, result)))
