import sys
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
    
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

swapped = True
while swapped:
    swapped = False
    for i in range(N - 1):
        if is_even(arr[i]) and is_even(arr[i+1]):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        elif not is_even(arr[i]) and not is_even(arr[i+1]):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

print(*arr)

            

