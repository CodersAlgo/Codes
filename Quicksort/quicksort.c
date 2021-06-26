#include <stdio.h>

int quicksort();
int partition();

int main(){
    int array[7] = {10,20,78,1,4,9,0};
    int length = sizeof(array)/sizeof(array[0]);
    quicksort(array , 0 ,length);
    printf("Sorted form of given input array in ascending order is :- \t");
    for(int x=0;x<length;x++){
        printf("%d\t",array[x]);
    }
    printf("\n");
    return 0;
}

int quicksort(int array[] , int l , int r){
    int j;
    if(l<r){
        j = partition(array,l,r);
        quicksort(array,l,j);
        quicksort(array,j+1,r);
    }
    return 0;
}

int partition(int array[],int l , int r){
    int i , j , pivot , temp;
    pivot = array[l];
    i = l;
    j = r;
    do{
        do{
            i++ ; 
        } while(array[i] <= pivot);

        do{
            j -- ;
        } while(array[j] > pivot);

        if(i < j) {
            temp = array[j];
            array[j] = array[i];
            array[i] = temp;
        }
    } while(i < j);

    temp = array[j];
    array[j] = pivot;
    array[l] = temp;
    return j;
}