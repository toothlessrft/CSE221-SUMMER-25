n,m=map(int,input().split())
l=list(map(lambda _:[0]*n,range(n)))
for i in range(m):
  x,y,z=map(int,input().split())
  l[x-1][y-1]=z
for i in l:
  print(' '.join(map(str, i)))
