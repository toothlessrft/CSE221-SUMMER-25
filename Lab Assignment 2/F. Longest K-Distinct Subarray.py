import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

max_len = 0
left = 0
freq = {}
d_idx = 0
for right in range(n):
    if arr[right] not in freq or freq[arr[right]] == 0:
        d_idx += 1
        freq[arr[right]] = 1
    else:
        freq[arr[right]] += 1

    while d_idx > k:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            d_idx -= 1
        left += 1

    if right - left + 1 > max_len:
        max_len = right - left + 1

print(max_len)
