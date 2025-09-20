import sys
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

s_tuple = sorted(zip(arr, range(len(arr))))
arr_sorted = sorted(arr)

def solve():
    for i in range(n - 2):
        x = i
        l, r = i + 1, n - 1
        while l < r:
            current_sum = arr_sorted[x] + arr_sorted[l] + arr_sorted[r]
            if current_sum == k:
                return x, l, r 
            elif current_sum < k:
                l += 1
            else:
                r -= 1
    return None

result = solve()
if result is None:
    print(-1)
else:
    x, y, z = result
    x_orig = s_tuple[x][1] + 1
    y_orig = s_tuple[y][1] + 1
    z_orig = s_tuple[z][1] + 1
    print(x_orig, y_orig, z_orig)
