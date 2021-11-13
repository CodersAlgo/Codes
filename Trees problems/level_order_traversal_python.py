import queue

class node() :
  def __init__(self,data) :
    self.data = data
    self.left = None
    self.right = None

#level order traversal python
def level_order_input() : # taking the input of binary tree level wise
  q = queue.Queue()
  root = int(input("Enter the value of root :- "))
  if root == -1 :
    return None
  root = node(root)
  q.put(root)
  while not q.empty() :
    temp = q.get()
    left = int(input(f"Enter the left child of {temp.data}:- "))
    if left != -1 :
      temp.left = node(left)
      q.put(temp.left)
    right = int(input(f"Enter the right child of {temp.data}:- "))
    if right != -1 :
      temp.right = node(right)
      q.put(temp.right)
  return root

def print_level_wise(root) :
  if root == None :
    return
  q = queue.Queue() # using the queue data structure
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

root = level_order_input() # enter -1 if node is not present
print_level_wise(root) # pass the root of binary tree as argument
