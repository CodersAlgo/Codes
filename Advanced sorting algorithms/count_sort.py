import numpy as np

def count_sort(array) :
  max = array.max()
  index_array = np.array([0]*(max+1))
  for x in array :
    index_array[x] += 1
    # print(index_array)
  # print("Index array",index_array)
  x = 0
  y = 0
  while x < max+1 :
    if index_array[x] != 0 :
      array[y] = x
      y += 1
      index_array[x] -= 1
    else :
      x += 1
  return array

array = np.array([1,8,9,10,3,7,8,8,1,2])
print("Given array is ",array)
sorted_array = count_sort(array)
print("Array after sorting using count sort is ",sorted_array)
