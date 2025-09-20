from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

def cycle_detection(s):
    vis[s] = 1

    for neighbor in graph[s]:
        if vis[neighbor] == 0:
            if cycle_detection(neighbor):
                return True
        elif vis[neighbor] == 1:
            return True
    vis[s] = 2
    return False


vis = [0] * (n + 1)
for node in range(1, n + 1):
    if not vis[node]:
        if cycle_detection(node):
            print("YES")
            exit()
print("NO")
