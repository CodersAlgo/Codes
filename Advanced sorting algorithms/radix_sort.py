import numpy as np

class node() :
  def __init__(self,value) :
    self.value = value
    self.next = None

class linked_list() :

  def __init__(self) :
    self.head =None

  def insert(self,value) :
    if self.head == None :
      self.head = node(value)
    else :
      temp = self.head
      while temp.next :
        temp = temp.next
      temp.next = node(value)

  def delete(self) :
    temp = self.head
    if temp :
      deleted_value = temp.value
      if temp.next :
        self.head = temp.next
        del temp
      else :
        self.head = None
        del temp
      return deleted_value
    else :
      return None

  def print_ll(self) :
    temp = self.head
    while temp :
      print(temp.value,"-->",end="")
      temp = temp.next

def radix_sort(array) :

  radix_array = np.array([None]*len(array))
  for x in range(len(array)) :
    radix_array[x] = linked_list()

  max_value = array.max()
  len_max_value = len(str(max_value))

  z = 1
  while len_max_value != 0 :
    y = 10
    for x in array :
      temp = (x//z)%y
      radix_array[temp].insert(x)

    w = 0
    x = 0

    while w < len(array) :
      while radix_array[w].head != None :
        array[x] = radix_array[w].delete()
        x += 1
      w += 1

    len_max_value -= 1
    z *= 10
  return array


array = np.array([101,158,59,210,33,67,118,158,11,32])
print("Given array is ",array)
sorted_array = radix_sort(array)
print("Array after sorting using algorithm for radix sort is ",sorted_array)
