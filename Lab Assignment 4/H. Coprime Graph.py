import sys
def gcd(a,b):
  while b:
    a,b=b,a%b
  return a
n,m=map(int,sys.stdin.readline().split())
l=[]
for i in range(1,n+1):
  ng=[]
  for j in range(1,n+1):
    if i!=j and gcd(i,j)==1:
      ng.append(j)
  l.append(ng)
for _ in range(m):
  x,k=map(int,sys.stdin.readline().split())
  if k > len(l[x-1]):
    print(-1)
  else:
    print(l[x-1][k-1])
