def bubble_sort(array) :

    for x in range(len(array)-1) :

        for y in range(len(array)-1-x) :

            if array[y] > array[y+1] :
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
                
    return array

array = [5,1,7,2,9,0]
sorted_array = bubble_sort(array)
print("Array after sorting is ",sorted_array)