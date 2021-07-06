#include<stdio.h>

int binary_search(int array[], int left, int right, int search_element);

int main()
{
    int array[] = {2,3,5,7,9,10,12,13,15,16,19,20};
    // array sorted in ascending order 
    int search_element = 2 ;
    int index = binary_search(array,0,(sizeof(array)/sizeof(array[0]))-1,search_element);
    if (index != -1)
    printf("search element present at index %d\n",index);
    else
    printf("Given search element not present\n");
    return 0;
}

int binary_search(int array[], int left, int right, int search_element)
{ 

if ( left <= right ) 
{

int mid = ( left+right ) /2 ;
if ( array[mid] == search_element )
return mid ;
else if ( array[mid] > search_element )
return binary_search(array, left, mid-1, search_element) ;
else 
return binary_search(array, mid+1, right, search_element) ;

}

// If given element not fount returning -1
return -1;
}