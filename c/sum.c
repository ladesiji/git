#include <stdlib.h>
#include <stdio.h>

int main(int argc,char *argv[])
{
	int i,sum = 0;

	//判断是否输入两个以上参数
	
	if (argc<2)
		return 1;

	//将参数求和
	
	for (i=0;i<argc;i++)
		sum += atoi(argv[i]);

	printf("sum=%d\n",sum);
	return 0;
}
