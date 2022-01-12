from queue import Queue

class node :

    def __init__(self,data) :
        self.data = data
        self.next = []

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

def print_tree(root) :
    if not root :
        return
    print(root.data,":",end = " ")
    for x in root.next :
        print(x.data,end = "  ")
    print()
    for x in root.next :
        print_tree(x)
