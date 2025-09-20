import sys
from collections import deque
N = int(sys.stdin.readline())
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
if (x1, y1) == (x2, y2):
    print(0)
    sys.exit()

if N < 3 or max(x1, y1, x2, y2) > N:
    print(-1)
    sys.exit()

if N == 3 and ((x1 == y1 == 2) or (x2 == y2 == 2)):
    print(-1)
    sys.exit()

moves = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
front = deque([(x1, y1)])
back = deque([(x2, y2)])
dist_front = [[-1] * (N + 1) for _ in range(N + 1)]
dist_back = [[-1] * (N + 1) for _ in range(N + 1)]
dist_front[x1][y1] = 0
dist_back[x2][y2] = 0

while front and back:
    if len(front) <= len(back):
        queue, curr, other = front, dist_front, dist_back
    else:
        queue, curr, other = back, dist_back, dist_front

    for _ in range(len(queue)):
        cx, cy = queue.popleft()
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if not (1 <= nx <= N and 1 <= ny <= N):
                continue
            if curr[nx][ny] != -1:
                continue
            if other[nx][ny] != -1:
                print(curr[cx][cy] + 1 + other[nx][ny])
                sys.exit()
            curr[nx][ny] = curr[cx][cy] + 1
            queue.append((nx, ny))
