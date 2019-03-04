#include<stdio.h>
             
int main()
{
    char letter;
    scanf("%c",&letter);
    
    if((letter>='A')&&(letter<='Z'))
    {
        letter+='a'-'A';
        printf("You entered an uppercase %c.\n",letter);
    }
    else {
        printf("You did not enter an uppercase letter.\n");
    }
    
    return 0;
}
