#include<stdio.h>
              
int main()
{
   int i,sum=0;
   printf("please enter i:");
   scanf("%d",&i);
   while(i<=100)
   {
       sum=sum+i;
       i++;
   }
   printf("sum=%d\n",sum);
    
    return 0;
}