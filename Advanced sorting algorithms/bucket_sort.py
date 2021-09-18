import numpy as np

class node() :
  def __init__(self,value) :
    self.value = value
    self.next = None

class linked_list() :

  def __init__(self) :
    self.head = None

  def insert(self,value) :
    if not self.head :
      self.head = node(value)
    else :
      temp = self.head
      while temp.next :
        temp = temp.next
      temp.next = node(value)

  def delete(self) :
    temp = self.head
    if temp :
      del_value = temp.value
    else :
      return None

    if temp.next :
      self.head = temp.next
      del temp
    else :
      self.head = None

    return del_value

  def print_ll(self) :
    temp = self.head
    while temp :
      print(temp.value)
      temp = temp.next

def bucket_sort(unsorted_array) :
  max = unsorted_array.max()
  bin_array = np.array([None]*(max+1))
  for x in range(len(bin_array)) :
    bin_array[x] = linked_list()
  for x in unsorted_array :
    bin_array[x].insert(x)
  i = 0
  j = 0
  while i < (max+1) :
    while bin_array[i].head != None :
      unsorted_array[j] = bin_array[i].delete()
      j += 1
    i += 1
  return unsorted_array

array = np.array([1,8,9,10,3,7,8,8,1,2])
print("Given array is ",array)
sorted_array = bucket_sort(array)
print("Array after sorting using algorithm for bucket sort is ",sorted_array)
