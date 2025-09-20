import sys
def build_order(a,l,r,new_order):
  if l > r:
    return
  mid=(l+r)//2
  new_order.append(a[mid])
  build_order(a,l,mid-1,new_order)
  build_order(a,mid+1,r,new_order)
new_order=[]
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
build_order(a,0,n-1,new_order)
print(" ".join(map(str,new_order)))
