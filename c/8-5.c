#include<stdio.h>
#include<string.h>

int main()
{
   char str[]="China\nChengdu";
   
   puts(str);
   printf("Enter a new string:");
   gets(str);
   puts(str);
   
   return 0;
}
