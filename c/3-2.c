#include<stdio.h>                
int main()
{
   float tank_volume;
   float oil_density;
   float oil_kg;
   float area;
   
   tank_volume=0.1;
   oil_density=850;
   
   oil_kg=tank_volume*oil_density;
   area=oil_kg/0.85;
   printf("Most farming is %f mu",area);
   return 0;
}