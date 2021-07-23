 #include <stdio.h>
#include<stdlib.h>

void Insertion(int A[],int n)
{
int i,j,x;

for(i=1;i<n;i++)
{
j=i-1;
x=A[i];

while(j>-1 && A[j]>x)
{
A[j+1]=A[j];
j--;
}

A[j+1]=x;
}
}

int main() {
int A[]={1,-1,9,0,-3,6,10,20,67,-9,8,8},n=sizeof(A)/sizeof(int),i;
Insertion(A,n);

printf("Array after sorting with insertion sort algorithm :- [");
for(i=0;i<n;i++)
printf("%d ",A[i]);

printf("]\n");
return 0;
}