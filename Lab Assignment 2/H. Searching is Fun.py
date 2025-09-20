import sys

def find_kth_number(k, x):
    return k + (k - 1) // (x - 1)

T = int(sys.stdin.readline())
results = []
for _ in range(T):
    k, x = map(int, sys.stdin.readline().split())
    results.append(find_kth_number(k, x))

print(*results)
