import sys
def merge(a, b):
  global inv
  i,j,m=0,0,[]
  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      m.append(a[i])
      i += 1
    else:
      m.append(b[j])
      inv+=len(a) - i
      j += 1
  m += a[i:]
  m += b[j:]
  return m
def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    return merge(a1, a2)
inv=0
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
sa = mergeSort(a)
print(inv)
print(*sa)
