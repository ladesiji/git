#include <stdio.h>

int main()
{
	int hole[10],n,i;

	for (i=0;i<10;i++)
		hole[i] = 0;

	for (n=0,i=0;i<1000;i++)
	{
		n = n % 10;
		hole[n] += 1;
		n += i + 2;
	}
	
	printf("the hole is:\n");
	for (i=0;i<10;i++)
		if(hole[i]==0)
			printf("%d\n",i);
	
	return 0;
}
