#include<stdio.h>                
int main()
{
   float radius,diameter;
   float circumference,area;
   float pi=3.1415926;
   
   printf("Input the diameter of the table:");
   scanf("%f",&diameter);
   
   radius=diameter/2.0;
   circumference=2.0*pi*radius;
   area=pi*radius*radius;
   printf("\nThe circumference is %f",circumference);
   printf("\nThe area is %f",area);
   
   return 0;
}