import sys
def make_postorder(l,r):
  global pre_index,postorder
  if l>r:
    return []
  root=preorder[pre_index]
  pre_index+=1
  idx=in_index[root]
  ls=make_postorder(l,idx-1)
  rs=make_postorder(idx+1,r)
  return ls+rs+[root]
n=int(sys.stdin.readline().strip())
inorder=list(map(int,sys.stdin.readline().split()))
preorder=list(map(int,sys.stdin.readline().split()))
in_index={val:i for i,val in enumerate(inorder)}
pre_index=0
postorder=[]
postorder=make_postorder(0,n-1)
print(" ".join(map(str,postorder)))
