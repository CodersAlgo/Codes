def partition(array,left_index,right_index) :
    pivot = array[left_index]
    i = left_index
    j = right_index
    while True :
        
        while True :
            i += 1
            if i == right_index or array[i] > pivot :  # array[i] < pivot for descending order
                break
                
        while True : 
            j -= 1
            if array[j] <= pivot : # array[j] >= pivot for descending order
                break
                
        if i < j :
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        
        if i > j :
            break
    
    temp = array[j]
    array[j] = array[left_index]
    array[left_index] = temp
    
    return j

def quicksort(array , left_index , right_index) :
    if left_index < right_index :
        partion_index = partition(array,left_index,right_index)
        quicksort(array,left_index,partion_index)
        quicksort(array,partion_index+1,right_index)
        
array = list(map(int,input("enter space separated elements as input :- ").split(" ")))
quicksort(array,0,len(array))
print("sorted input array in ascending order is :- ",array)