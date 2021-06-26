#include<stdio.h>

int main()
{
    int a[5] = {10,6,90,8,-1};
    int sum = 0 ;
    float average ; 
    for(int x =0 ; x< sizeof(a)/sizeof(int);x++)
    {
        sum += a[x];
    }
    average = (float)sum/(sizeof(a)/sizeof(int));
    printf("\nSum of elements in given array is :- %d\n\n",sum);
    printf("\naverage of elements in given array is :- %.2f\n\n",average);
    return 0;
}