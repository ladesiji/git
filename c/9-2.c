#include<stdio.h>

int main()
{
    int max(int x,int y);
    int a=10,b=20;
    int c;
    c=max(a,b);
    printf("%d",c);
        
    return 0;
}

int max(int x,int y)
{
    int z;
    z=x>y?x:y;
    return (z);
}