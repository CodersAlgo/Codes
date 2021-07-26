#include<stdio.h>

int linear_search(int array[],int search_element,int y);

int main()
{
    int array[] = {2,4,1,7,0,25,66,16,-5,-2,19,5};
    int index = linear_search(array,-5,sizeof(array)/sizeof(array[0]));
    if(index != -1)
    printf("element found by algorithm linear search at index %d\n",index);
    else
    printf("element not present in given array\n");
    return 0;
}

int linear_search(int array[],int search_element,int y) {
    y -= 1;
    for(int x=0;x<=y;x++) {
        if(array[x] == search_element)
        return x;
        if(array[y] == search_element)
        return y;
        y -= 1;
    }
    return -1;
}
