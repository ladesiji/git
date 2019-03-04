#include<stdio.h>

int main()
{
    void exchange(int *q1,int *q2,int *q3);
    int a,b,c,*p1,*p2,*p3;
    printf("please enter 3 integer number:");
    scanf("%d%d%d",&a,&b,&c);
    p1=&a;
    p2=&b;
	p3=&c;
    exchange(p1,p2,p3);
	printf("the order is :%d,%d,%d\n",a,b,c);
    return 0;
}

void exchange(int *q1,int *q2,int *q3)
{
	void swap(int *pt1,int *pt2);
	if(*q1<*q2) swap(q1,q2);
	if(*q1<*q3) swap(q1,q2);
	if(*q2<*q3) swap(q2,q3);
}

void swap(int *pointer_1,int *pointer_2)
{
    int temp;
    temp=*pointer_1;
    *pointer_1=*pointer_2;
    *pointer_2=temp;
}
