import sys
N = int(sys.stdin.readline())
id = list(map(int, sys.stdin.readline().split()))
marks = list(map(int, sys.stdin.readline().split()))
s_count = 0

def array_sort(id, marks, s_count):
    for i in range(N):
        max_idx = i
        for j in range(i+1, N):
            if marks[j] > marks[max_idx] or (marks[j] == marks[max_idx] and id[j] < id[max_idx]):
                max_idx = j
        if max_idx != i:
            marks[i], marks[max_idx] = marks[max_idx], marks[i]
            id[i], id[max_idx] = id[max_idx], id[i]
            s_count += 1
    return id, marks, s_count

if N == 1:
    print(f'Minimum swaps: {s_count}')
    for i in range(N):
        print(f'ID: {id[i]} Mark: {marks[i]}')
else:
    id, marks, s_count = array_sort(id, marks, s_count)
    print(f'Minimum swaps: {s_count}')
    for i in range(N):
        print(f'ID: {id[i]} Mark: {marks[i]}')
    
