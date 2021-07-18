#include <stdio.h>
#include<stdlib.h>

void Bubble(int A[],int n)
{
int i,j,temp,flag;

for(i=0;i<n-1;i++)
{
flag = 0;

for(j=0;j<n-i-1;j++)
{

if(A[j]>A[j+1])
{
temp = A[j];
A[j] = A[j+1];
A[j+1] = temp;
flag = 1;
}
}

if(flag == 0 )
{
    break;
}
}
}

int main()
{
int A[]={1,2,3,4,5,6},i;
Bubble(A,sizeof(A)/sizeof(int));

printf("Array after sorting is [ ");
for(i=0;i<sizeof(A)/sizeof(int);i++)

printf("%d ",A[i]);
printf("]\n");

return 0;
}