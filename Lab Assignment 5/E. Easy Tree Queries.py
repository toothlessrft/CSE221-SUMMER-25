from collections import defaultdict
import sys
sys.setrecursionlimit(300000) 
n, r  = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

subtree = [0] * (n + 1)
def dfs(node, parent):
    subtree[node] = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            subtree[node] += subtree[neighbor]
        

dfs(r, -1)
q = int(sys.stdin.readline())
for _ in range(q):
        a = int(sys.stdin.readline())
        print(subtree[a])
