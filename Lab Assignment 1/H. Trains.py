import sys

def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

N = int(sys.stdin.readline())
train = []
time = []
dest = []
original_idx = []

for i in range(N):
    parts = sys.stdin.readline().split()
    train.append(parts[0])
    time.append(parts[-1])
    dest.append(parts[4])
    original_idx.append(i)

def array_sort(time, train, dest, original_idx):
    time_mins = [time_to_minutes(t) for t in time]
    combined = list(zip(train, time_mins, time, dest, original_idx))
    combined.sort(key=lambda x: (x[0], -x[1], x[4]))

    train = [x[0] for x in combined]
    time = [x[2] for x in combined]
    dest = [x[3] for x in combined]
    
    return time, train, dest

time, train, dest = array_sort(time, train, dest, original_idx)
for i in range(N):
    print(f'{train[i]} will departure for {dest[i]} at {time[i]}')
