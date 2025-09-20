import sys
n, m, k = map(int, sys.stdin.readline().split())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))

l, r = 0, (m-1)
min_l , min_r = l, r
m_diff = abs(arr1[min_l] + arr2[min_r] - k)
found = False
while l < n and r >= 0:
    sum = arr1[l] + arr2[r]
    c_diff = abs(arr1[l] + arr2[r] - k)
    if sum == k:
        print(l+1, r+1)
        found = True
        break
    if c_diff < m_diff:
        m_diff = c_diff
        min_l = l
        min_r = r
    if k > sum:
        l += 1
    else:
        r -= 1

if not found:
    print(min_l+1, min_r+1)

    
