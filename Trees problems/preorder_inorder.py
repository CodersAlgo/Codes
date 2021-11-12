import queue

class node() :
  def __init__(self,data) :
    self.data = data
    self.left = None
    self.right = None

def print_level_wise(root) :
  if root == None :
    return
  q = queue.Queue()
  q.put(root)
  while not q.empty() :
    temp = q.get()
    print(temp.data,end = ":")
    if temp.left :
      print("L ",temp.left.data,end = " ")
      q.put(temp.left)
    if temp.right :
      print("R ",temp.right.data,end = " ")
      q.put(temp.right)
    print()

# construct tree from given inorder and preorder traversals

def build_pre_in(pre,ino) :
  if len(pre) == 0 or len(ino) == 0 :
      return None
  root = node(pre[0])
  l = 0
  while l <= len(pre) :
      if l == len(pre) :
          return None
      if ino[l] == root.data :
          break
      l += 1
  l_pre = pre[1:l+1]
  r_pre = pre[l+1:]
  l_ino = ino[:l]
  r_ino = ino[l+1:]
  root.left = build_pre_in(l_pre,l_ino)
  root.right = build_pre_in(r_pre,r_ino)
  return root

pre = [1,2,4,5,3,6,7]
ino = [4,2,5,1,6,3,7]
root = build_pre_in(pre,ino)
print_level_wise(root)
