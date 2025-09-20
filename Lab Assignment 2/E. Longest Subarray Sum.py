import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

max_len = 0
current_sum = 0
left = 0

for right in range(n):
    current_sum += arr[right]
    while current_sum > k and left <= right:
        current_sum -= arr[left]
        left += 1
    if current_sum <= k:
        max_len = max(max_len, right - left + 1)

print(max_len)
