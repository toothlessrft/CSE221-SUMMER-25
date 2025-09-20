import sys

len_lst, t_sum = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if len_lst == 1:
    print(-1)
else:
    found = False
    for i in range(len_lst):
        j = binary_search(arr, t_sum - arr[i], i + 1, len_lst - 1)
        if j != -1:
            print(i + 1, j + 1)
            found = True
            break

    if not found:
        print(-1)
