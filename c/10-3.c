#include<stdio.h>

int main()
{
    void swap(int *pointer_1,int *pointer_2);
    int *p1,*p2,a,b;
    printf("please enter two integer number:");
    scanf("%d,%d",&a,&b);
    p1=&a;
    p2=&b;
    if(a<b)
        swap(p1,p2);
	printf("max=%d,min=%d\n",a,b);
    return 0;
}

void swap(int *pointer_1,int *pointer_2)
{
    int temp;
    temp=*pointer_1;
    *pointer_1=*pointer_2;
    *pointer_2=temp;
}
