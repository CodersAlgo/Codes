#include<stdio.h>

int binary_search();

int main()
{
    int a[5] = {1,0,9,7,5};
    int index,search;
    search = 9;
    index = binary_search(a,search,sizeof(a)/sizeof(int));
    if (index != -1 ){
        printf("given element is found at index %d \n",index);
    }
    else{
        printf("Given element is not found in array");
    }
    return 0;
}

int binary_search(int a[],int search,int size)
{
    for(int x=0;x<size;x++)
    {
        if ( a[x] == search ){
            return x;
        }
    }
    return -1;
}