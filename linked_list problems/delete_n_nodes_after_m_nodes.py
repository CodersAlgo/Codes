class node() :

  def __init__(self,value) :
    self.value = value
    self.next = None

class LinkedList() :

  def __init__(self) :
    self.head = None
    self.tail = None

  def insert(self,value) :
    if self.head == None :
      self.head = node(value)
      self.tail = self.head
    else :
      self.tail.next = node(value)
      self.tail = self.tail.next

  def print_ll(self) :
    temp = self.head
    while temp :
      print(temp.value,"--->",end = " ")
      temp = temp.next
    print(None)

def delete_n(head,n,m) :

  h1 = head

  n1 = 0
  m1 = 0

  while True :

    while head and m1 < m :
      prev = head
      head = head.next
      m1 += 1

    temp = head

    while head and n1 < n :
      temp = temp.next
      del head
      head = temp
      n1 += 1

    prev.next = head

    if not temp :
      break
    n1 = 0
    m1 = 0

  return h1

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)
h1 = delete_n(ll.head,3,2)
while h1 :
  print(h1.value,end = "\t")
  h1 = h1.next
