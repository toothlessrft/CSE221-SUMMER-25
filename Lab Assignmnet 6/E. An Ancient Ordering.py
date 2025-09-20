import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

adj = defaultdict(list)
indegree = defaultdict(int)
letters = set()

for i in range(n - 1):
    w1, w2 = words[i], words[i + 1]
    if len(w1) > len(w2) and w1.startswith(w2):
        print(-1)
        sys.exit()

    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            adj[c1].append(c2)
            indegree[c2] += 1
            break
for w in words:
    for c in w:
        letters.add(c)
pq = []
for c in letters:
    if indegree[c] == 0:
        heapq.heappush(pq, c)

result = []
while pq:
    u = heapq.heappop(pq)
    result.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(pq, v)
if len(result) != len(letters):
    print(-1)
else:
    print("".join(result))
