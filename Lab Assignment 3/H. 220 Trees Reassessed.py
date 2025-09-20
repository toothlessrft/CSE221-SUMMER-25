import sys

def split_tree(in_s, post_s):
    stack = []
    task = [(in_s, post_s)]
    result = []
    
    while task:
        ino, post = task.pop()
        if not ino:
            continue
        root = post[-1]
        result.append(root)
        idx = ino.index(root)
        left_in = ino[:idx]
        right_in = ino[idx+1:]
        left_post = post[:len(left_in)]
        right_post = post[len(left_in):-1]
        if right_in:
            task.append((right_in, right_post))
        if left_in:
            task.append((left_in, left_post))
    return result

n = int(sys.stdin.readline())
i_seq = list(map(int, sys.stdin.readline().split()))
p_seq = list(map(int, sys.stdin.readline().split()))
order = split_tree(i_seq, p_seq)
print(' '.join(map(str, order)))
