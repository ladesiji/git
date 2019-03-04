#include<stdio.h>
              
int main()
{
  int i,j,t,LearnTime[10];
  printf("please enter 10 number:\n");
  
  for(i=0;i<10;i++)
      scanf("%d",&LearnTime[i]);
  
  for(j=0;j<9;j++)
      for(i=0;i<9-j;i++)
          if(LearnTime[i]>LearnTime[i+1])
          {
              t=LearnTime[i];
              LearnTime[i]=LearnTime[i+1];
              LearnTime[i+1]=t;
          }
   printf("the sorted number:\n");
   for(i=0;i<10;i++)
       printf("%d\t",LearnTime[i]);
   
      
   return 0;
}