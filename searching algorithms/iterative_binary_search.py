# Assuming that input array is in ascending order

def binary_search(array,search_element) :
    left = 0
    right = len(array)-1
    while left<=right :
        mid = (left+right)//2
        if array[mid] == search_element :
            return mid
        elif array[mid] > search_element :
            right = mid-1
        else :
            left = mid+1
    return None
            
array = [2,3,5,7,9,10,12,13,15,16,19,20]
search_element = 2
index = binary_search(array,search_element)
if index != None :
    print("search element is present at index",index)
else :
    print("Given search element not present \n")