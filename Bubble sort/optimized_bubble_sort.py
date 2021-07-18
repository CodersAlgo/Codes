def bubble_sort(array) :

    for x in range(len(array)-1) :
        flag = 0

        for y in range(len(array)-1-x) :

            if array[y] > array[y+1] :
                temp = array[y]
                array[y] = array[y+1]
                array[y+1] = temp
                flag = 1

        if flag == 0 :
            break
        
    return array

array = [1,2,3,4,5,6]
sorted_array = bubble_sort(array)
print("Array after sorting is ",sorted_array)