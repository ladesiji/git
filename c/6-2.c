#include<stdio.h>
              
int main()
{
    int number;
    printf("\nPlease enter an integer between 1 and 10:");
    scanf("%d",&number);
    if(number>5)
        printf("You entered %d which is greater than 5\n",number);
    
    if(number<6)
        printf("You entered %d which is less than 6\n",number);
    
    return 0;
}
