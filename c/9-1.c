#include<stdio.h>
#include<string.h>

int main()
{
    void printstar();
    void print_message();
    printstar();
    print_message();
    printstar();
        
    return 0;
}

void printstar(){
    printf("**************\n");
}

void print_message(){
    printf("how do you do!\n");
}