import sys 
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    arr  = list(map(int, sys.stdin.readline().split(" ")))

    flag = False
    if N == 1:
        flag = True

    for j in range(N-1):
        if (arr[j] <= arr[j+1]):
            flag = True
        else:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
            

