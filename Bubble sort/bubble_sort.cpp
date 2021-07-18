#include <stdio.h>
#include<stdlib.h>

void Bubble(int A[],int n)
{
int i,j,temp;

for(i=0;i<n-1;i++)
{

for(j=0;j<n-i-1;j++)
{

if(A[j]>A[j+1])
{
temp = A[j];
A[j] = A[j+1];
A[j+1] = temp;
}

}
}
}

int main()
{
int A[]={5,1,7,2,9,0},i;
Bubble(A,sizeof(A)/sizeof(int));
printf("Array after sorting is [ ");
for(i=0;i<sizeof(A)/sizeof(int);i++)
printf("%d ",A[i]);
printf("]\n");
return 0;
}