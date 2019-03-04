#include<stdio.h>
int main()
{
    int i,*p,a[10];
    p=a;
    printf("please enter 10 integer numbers:");
    for(i=0;i<10;i++)
        scanf("%d",p++);
    
    for(i=0;i<10;i++,p++)
        printf("%d\t",*p);
	printf("\n");
    
    return 0;
}