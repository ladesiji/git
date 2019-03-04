#include<stdio.h>
int main()
{
    int a[10];
    int i,*p;
    printf("please enter 10 integer numbers:");
    for(i=0;i<10;i++)
        scanf("%d",&a[i]);
    
    for(p=a;p<(a+10);p++)
        printf("%d\t",*p);
    
    return 0;
}