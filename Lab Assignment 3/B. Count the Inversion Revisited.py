import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j] ** 2:
            count += 1
print(count)
