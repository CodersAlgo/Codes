def bubble_sort(array) :
    x = 0
    while x < len(array)-1 :
        y = 0
        flag = 0

        while y < len(array)-1-x :

            if array[y] > array[y+1] :
                array[y] , array[y+1] = array[y+1] , array[y]
                flag = 1
            y += 1

        if flag == 0:
            break

        x += 1

    return array


print("enter the list of elements in space seprated format :- ")
array = list(map(int,input().split(" ")))

sorted_array = bubble_sort(array)

print("Array after sorting is ",sorted_array)
