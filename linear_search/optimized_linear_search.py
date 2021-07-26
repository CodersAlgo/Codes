def linear_search(array,search_elelemnt) :
    y = len(array)-1
    for x in range(y+1) :
        if array[x] == search_elelemnt :
            return x
        if array[y] == search_elelemnt :
            return y
        y -= 1
    return -1


array = [2,4,1,7,0,25,66,16,-5,-2,19,5]
index = linear_search(array,-5)
if(index!=-1) :
    print("element found by algorithm linear search at index ",index)
else :
    print("element not present in given array")