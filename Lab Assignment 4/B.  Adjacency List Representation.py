n,m=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
l=[[] for _ in range(n)]
for i in range(m):
  l[u[i]-1].append((v[i],w[i]))
for i in range(n):
  print(f'{i+1}:',*l[i], sep=" ")
