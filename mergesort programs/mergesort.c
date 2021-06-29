#include <stdio.h>
#include<stdlib.h>
void swap(int *x,int *y)
{
 int temp=*x;
 *x=*y;
 *y=temp;
}

void Merge(int A[],int l,int mid,int h)
{
 int i=l,j=mid+1,k=l;
 int B[100];

 while(i<=mid && j<=h)
 {
 if(A[i]<A[j])
 B[k++]=A[i++];
 else
 B[k++]=A[j++];
 }
 while(i<=mid)
 B[k++]=A[i++];
 while(j<=h)
 B[k++]=A[j++];

 for(i=l;i<=h;i++)
 A[i]=B[i];
}

void MergeSort(int A[],int l,int h)
{
 int mid;
 if(l<h)
 {
 mid=(l+h)/2;
 MergeSort(A,l,mid);
 MergeSort(A,mid+1,h);
 Merge(A,l,mid,h);

 }
}

int main()
{
 int A[]={1,3,2,7,4,8,0,5},n=8,i;

 MergeSort(A,0,n);

  printf("Sorted array is :- ");

 for(i=1;i<9;i++)
 printf("%d ",A[i]);
 printf("\n");

 return 0;
}