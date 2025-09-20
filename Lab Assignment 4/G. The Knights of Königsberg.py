import sys
n, m, k = map(int, sys.stdin.readline().split())
knights = set()
moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]


for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    knights.add((x, y))

for x, y in knights:
    for dx, dy in moves:
        if (x + dx, y + dy) in knights:
            print("YES")
            sys.exit()

print("NO")
