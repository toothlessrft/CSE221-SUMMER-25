import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

l = r = 0
while l<n and r<m:
    if arr1[l] < arr2[r]:
        print(arr1[l], end= ' ')
        l += 1
    else:
        print(arr2[r], end= ' ')
        r += 1

for i in range(l, n):
    print(arr1[i], end= ' ')
for i in range(r, m):
    print(arr2[i], end= ' ')

print()
