# Assuming that input array is in ascending order

def binary_search(array,left,right,search_element) :
    if left<=right :
        mid = (left+right)//2
        if array[mid] == search_element :
            return mid
        elif array[mid] > search_element :
            return binary_search(array,left,mid-1,search_element)
        else :
            return binary_search(array,mid+1,right,search_element)
        
array = [2,3,5,7,9,10,12,13,15,16,19,20]
search_element = 2
index = binary_search(array,0,len(array)-1,search_element)
if index != None :
    print("Given search element is present at index",index)
else :
    print("Given search element is not present in array")