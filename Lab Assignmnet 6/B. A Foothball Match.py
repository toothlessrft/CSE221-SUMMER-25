from collections import defaultdict
from queue import Queue
import sys

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

color = [-1] * (n + 1) # 1: blue, 0: red, -1: uncolored

def bipartite(graph):
    q = Queue()
    max_count = 0
    for node in range(1, n + 1):
        if color[node] == -1:
                blue = 0
                red = 0
                color[node] = 1
                blue += 1
                q.put(node)

                while not q.empty():
                    curr = q.get()
                    for nei in graph[curr]:
                        if color[nei] == -1:
                            if color[curr] == 1:
                                color[nei] = 0
                                red += 1
                            elif color[curr] == 0:
                                color[nei] = 1
                                blue += 1
                            q.put(nei)
                max_count += max(blue, red)
    return max_count

print(bipartite(graph))
