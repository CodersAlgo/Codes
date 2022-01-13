from queue import Queue

# structure of node of n array tree
class node :

    def __init__(self,data) :
        self.data = data
        self.next = []

# function to insert nodes into n array tree
def insert_nodes() :
    data = int(input("Enter the value of root :- "))
    if data != -1 :
        root = node(data)
    else :
        return
    q = Queue()
    q.put(root)
    while not q.empty() :
        value = q.get()
        children = int(input(f"Enter number of children for {value.data} :- "))
        for x in range(children) :
            data = int(input("Enter the value of child :- "))
            child = node(data)
            value.next.append(child)
            q.put(child)
    return root

# function to traverse n array tree level wise
def print_level_wise(root) :
    if root == None :
        return
    q = Queue()
    q.put(root)
    while not q.empty() :
        temp = q.get()
        print(temp.data,end = " : ")
        for x in temp.next :
            print(x.data,end = "    ")
            q.put(x)
        print()

# code to replace the value of node with its depth
def replace_with_depth(root,depth=0) :
    if root == None :
        return
    root.data = depth
    for x in root.next :
        replace_with_depth(x,depth+1)

root = insert_nodes()
print_level_wise(root)
replace_with_depth(root)
print_level_wise(root)
