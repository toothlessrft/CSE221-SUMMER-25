import sys
size = int(sys.stdin.readline())
n, m = map(int, sys.stdin.readline().split())
result = []
for i in range(n-1, n+2):
    for j in range(m-1, m+2):
        if (i > 0 and i <= size and j > 0 and j <= size) and (i, j) != (n, m):
            result.append((i, j)) 


print(len(result))
for i in result:
    print(i[0], i[1])
