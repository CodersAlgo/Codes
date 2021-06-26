#include <stdio.h>

int main(){
    // assigning values to an array
    int a[5] = {1,2,3} ;
    int b[5] = {} ;
    int c[5] = {1,2,3,4,5} ;
    int d[] = {1,2,3,4,5} ;
    int sizeofc = 5;
    printf("elements present in array a are :- \n\n");
    for(int x=0;x<sizeof(a)/sizeof(int);x++)
    {
        printf("%d\t",a[x]); // acessing elements in array using indexing
    }
    printf("\n\nelements present in array b ( garbage values ) are :- \n");
    for(int x=0;x<sizeof(b)/sizeof(int);x++)
    {
        printf("%d\t",b[x]);
    }
    printf("\n\nlength of array d is %lu \n\n",sizeof(d)/sizeof(int));
    // deleting element 4 in array c by assigning -1 
    c[3] = -1;
    printf("\n\nelements present in array c after deleting 4 are :- \n");
    for(int x=0;x<sizeofc;x++)
    {
        if (c[x] != -1) {
            printf("%d\t",c[x]);
        }
    }
    c[3] = 4;
    // deleting element 4 in array c by shifting elements 
    for(int x=3;x<sizeofc-1;x++)
    {
            c[x] = c[x+1];
    }
    sizeofc -= 1 ; //tracking last index of array c
    printf("\n\nelements present in array c after deleting 4 are :- \n");
    for(int x=0;x<sizeofc;x++)
    {
            printf("%d\t",c[x]);
    }
    printf("\n");
    return 0;
}