from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

vis = [0] * (n + 1)
stack = deque()
cycle = False

def dfs(u):
    global cycle
    vis[u] = 1
    for v in graph[u]:
        if vis[v] == 0:
            dfs(v)
            if cycle:
                return
        elif vis[v] == 1:
            cycle = True
            return
    vis[u] = 2
    stack.appendleft(u)

for i in range(1, n + 1):
    if vis[i] == 0:
        dfs(i)
        if cycle:
            break
if cycle:
    print(-1)
else:
    print(*stack)
