import numpy as np

def merge(left,mid,right,array) :
    x = z = left
    y = mid+1 
    sorted_array = np.array([None]*(right+1))
    while x <= mid and y <= right :
        if array[x] < array[y] :
            sorted_array[z] = array[x]
            z += 1
            x += 1
        else :
            sorted_array[z] = array[y]
            z += 1
            y += 1
    while x <= mid :
        sorted_array[z] = array[x]
        z += 1
        x += 1
    while y <= right :
        sorted_array[z] = array[y]
        z += 1
        y += 1
        
    x = left
    y = right
    while x <= y :
        array[x] = sorted_array[x]
        x += 1

def merge_sort(left,right,array) :
    if left < right :
        mid = (left + right)//2
        merge_sort(left,mid,array)
        merge_sort(mid+1,right,array)
        merge(left,mid,right,array)
        
array = [1,3,2,7,4,8,0,5]
merge_sort(0,len(array)-1,array)
print("sorted array is :- ", array)