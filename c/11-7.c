#include<stdio.h>
int main()
{
   void copy_string(char from[],char to[]);
   char *a="I am a teacher";
   char b[]="You are a programmer";
   char *p=b;
   
   printf("string a=%s\n string b=%s\n",a,b);
   printf("copy string a to string b:\n");
   copy_string(a,p);
   printf("\n string a=%s\n string b=%s\n",a,b);
   
   return 0;
}

void copy_string(char *from,char *to)
{
   for(;*from!='\0';from++,to++)
		*to=*from;
   *to='\0';
}
