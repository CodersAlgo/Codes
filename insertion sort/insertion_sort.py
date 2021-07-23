def insertion_sort(array) :
    for x in range(1,len(array)) :
        y = x
        temp = array[x]
        while y > 0 and temp < array[y-1] :
            array[y] = array[y-1]
            y -= 1
        array[y] = temp
    return array

array = [1,-1,9,0,-3,6,10,20,67,-9,8,8]
sorted_array = insertion_sort(array)
print("Array after sorting with insertion sort algorithm :- ",sorted_array)