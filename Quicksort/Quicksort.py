import numpy as np

def partition(array,low,high) :
    pivot = array[low]
    i = low + 1
    j = high
    while True :
        
        while True :
            if i > high or array[i] > pivot :
                break
            i += 1
            
        while True :
            if array[j] <= pivot :
                break
            j -= 1
            
        if i < j :    
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
        
        if i > j :
            break
        
    temp = array[low]
    array[low] = array[j]
    array[j] = temp
    return j

def quick_sort(array,low,high) :
    if low < high :
        j = partition(array,low,high)
        quick_sort(array,low,j)
        quick_sort(array,j+1,high)
        
array = [10,20,78,1,4,9,0]
quick_sort(array,0,len(array)-1)
print("sorted form of given input array in ascending order is :-",array)





