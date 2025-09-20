import sys

def dfs(grid, visited, start_row, start_col, R, H):
    stack = [(start_row, start_col)]
    diamonds = 0
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= R or y < 0 or y >= H or grid[x][y] == '#' or visited[x][y]:
            continue
        visited[x][y] = True
        if grid[x][y] == 'D':
            diamonds += 1
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            stack.append((x+dx, y+dy))
    return diamonds

R, H = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[False] * H for _ in range(R)]
max_diamonds = 0

for i in range(R):
    for j in range(H):
        if grid[i][j] != '#' and not visited[i][j]:
            max_diamonds = max(max_diamonds, dfs(grid, visited, i, j, R, H))

print(max_diamonds)
