def linear_search(array,search_element) :
    for x in range(len(array)) :
        if array[x] == search_element :
            return x
    return None

array = [1,2,3,4,5,6,7,8,9,10]
index = linear_search(array,0)
if index != None :
    print("Given search element is present at index",index)
else :
    print("Given search element is not present in array")