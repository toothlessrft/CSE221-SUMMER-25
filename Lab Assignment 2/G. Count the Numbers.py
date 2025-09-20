import sys

def binary_search(arr, target, find_first=True):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target or (find_first and arr[mid] == target):
            right = mid
        else:
            left = mid + 1
    return left


n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    left = binary_search(arr, x, True)
    right = binary_search(arr, y, False)
    print(right - left)
