import sys
from collections import deque, defaultdict
N, M, S, Q = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

sources = list(map(int, sys.stdin.readline().split()))
destinations = list(map(int, sys.stdin.readline().split()))

dist = [-1] * (N + 1)
queue = deque()
for s in sources:
    dist[s] = 0
    queue.append(s)

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)
ans = []
for d in destinations:
    ans.append(str(dist[d]))

print(" ".join(ans))
