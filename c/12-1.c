#include<stdio.h>
int main()
{
    FILE *fp;
	char ch,filename[10];
	printf("Please enter the file name");

	scanf("%s",filename);
	if((fp=fopen(filename,"w"))==NULL)
	{
		printf("Unabel to open this file\n");
		exit(0);
	}

	ch=getchar();
	printf("Please enter a string in the disk (Ends with a #):");
	ch=getchar();
	while(ch!='#')
	{
		fputc(ch,fp);
		putchar(ch);
		ch=getchar();
	}
	fclose(fp);
	putchar(10);
    return 0;
}
