def selection_sort(array) :
    for x in range(len(array)-1) :
        i = x
        for y in range(x+1,len(array)) :
            if array[i] > array[y] :
                i = y
        if i!= x :
            array[x] , array[i] = array[i] , array[x]
    return array

array = [5,1,7,2,9,0]
sorted_array = selection_sort(array)
print("Array after sorting using algorithm of selection sort :- ",sorted_array)