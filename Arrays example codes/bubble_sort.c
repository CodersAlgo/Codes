#include<stdio.h>

int main()
{
    int a[5] = {10,6,90,8,-1};
    for(int x=0;x<4;x++){
        for(int y=0;y<5-x-1;y++)
        {
            if (a[y]<a[y+1]){
                int temp = a[y];
                a[y] = a[y+1];
                a[y+1] = temp;
            }
        }
    }
    printf("Elements after sorting in descending order are :- \n\n");
    for(int x=0;x<5;x++)
    {
        printf("%d\t",a[x]);
    }
    printf("\n");
    return 0;
}