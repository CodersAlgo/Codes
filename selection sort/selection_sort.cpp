#include <stdio.h>
#include<stdlib.h>

void swap(int *x,int *y);
void selection_sort(int A[], int n);


int main()
{
int A[]={5,1,7,2,9,0},n=6,i;
selection_sort(A,n);

printf("Array after sorting using algorithm of selection sort :- \n[");

for(i=0;i<6;i++)
printf("%d ",A[i]);

printf("]\n");
return 0;

}

void swap(int *x,int *y)
{
int temp=*x;
*x=*y;
*y=temp;
}

void selection_sort(int A[],int n)
{
int i,j,k;

for(i=0;i<n-1;i++)
{
for(j=k=i;j<n;j++)
{
if(A[j]<A[k])
k=j;
}
swap(&A[i],&A[k]);
}
}