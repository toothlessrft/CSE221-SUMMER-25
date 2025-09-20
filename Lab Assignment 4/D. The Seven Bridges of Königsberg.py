import sys
n,m=map(int,sys.stdin.readline().split())
u=list(map(int,sys.stdin.readline().split()))
v=list(map(int,sys.stdin.readline().split()))
d=[0]*(n+1)
for a,b in zip(u, v):
  d[a]+=1
  d[b]+=1
c=0
for i in range(n):
  if d[i+1]%2!=0:
    c+=1
print("YES" if c==0 or c==2 else "NO")
