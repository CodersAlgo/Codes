import numpy as np

def shell_sort(array) :
  n = len(array)
  gap = n//2
  while gap >= 1 :
    for i in range(gap,n) :
      temp = array[i]
      j = i - gap
      while j >= 0 and array[j] > temp :
        array[j+gap] = array[j]
        j -= gap
      array[j+gap] = temp
    gap = gap//2
  return array

array = np.array([9,5,16,8,13,6,12,10,4,2,3])
print("Given array is ",array)
shell_sort(array)
print("Array after sorting using algorithm for Shell Sort is ",array)
