import sys
def solve():
    q = int(sys.stdin.readline())
    for _ in range(q):
        vals = list(map(int, sys.stdin.readline().split()))
        exp = int(sys.stdin.readline())
        res = matrix_power(vals, exp)
        print(res[0], res[1])
        print(res[2], res[3])

def matrix_power(mat, n):
    identity_matrix = [1, 0, 0, 1]
    base = mat[:]
    ans = identity_matrix
    while n > 0:
        if n & 1:
            ans = matrix_multiply(ans)
        base = matrix_multiply(base, base)
        n >>= 1
    return ans

def matrix_multiply(m1, m2):
    MOD = 10**9 + 7
    a = (m1[0]*m2[0] + m1[1]*m2[2]) % MOD
    b = (m1[0]*m2[1] + m1[1]*m2[3]) % MOD
    c = (m1[2]*m2[0] + m1[3]*m2[2]) % MOD
    d = (m1[2]*m2[1] + m1[3]*m2[3]) % MOD
    return [a, b, c, d]

solve()
