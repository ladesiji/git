#include<stdio.h>
              
int main()
{
  int n;
  for(n=100;n<=200;n++)
  {
      if(n%3==0)
          continue;
      printf("%d\t",n);
  }
  printf("\n");
    
    return 0;
}