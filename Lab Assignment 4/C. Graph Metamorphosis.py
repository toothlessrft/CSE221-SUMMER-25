import sys
n=int(sys.stdin.readline())
l=list(map(lambda _:[0]*n,range(n)))
for i in range(n):
  k,*m=map(int,sys.stdin.readline().split())
  for j in m:
    l[i][j]=1
for i in l:
  print(' '.join(map(str, i)))
