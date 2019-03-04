#include<stdio.h>
#include<string.h>

int main()
{
    char string[30];
    char ch[3][30];
    int i;
    for(i=0;i<3;i++)
        gets(ch[i]);
    strcpy(string,ch[0]);
    for(i=1;i<3;i++)
        if(strcmp(ch[i],string)<0)
            strcpy(string,ch[i]);
        printf("The result is :\n%s",string);
        
    return 0;
}