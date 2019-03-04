#include<stdio.h>
#include<string.h>

int main()
{
    char str1[30]="People's Republic of";
    char str2[]="china";
    printf("%s",strcat(str1,str2));
    return 0;
}