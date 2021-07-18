def bubble_sort(array) :

    for x in range(len(array)-1) :
        flag = 0

        for y in range(len(array)-1-x) :

            if array[y] > array[y+1] :
                array[y] , array[y+1] = array[y+1] , array[y]
                flag = 1

        if flag == 0 :
            break
        
    return array

print("enter the list of elements in space seprated format :- ")
array = list(map(int,input().split(" ")))

sorted_array = bubble_sort(array)

print("Array after sorting is ",sorted_array)