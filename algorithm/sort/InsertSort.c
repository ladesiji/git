#include<stdio.h>
#include<stdlib.h>

int n;

/*
 * 直接插入排序
 */

void InsertSort(int *array)
{
	int i, j;
	for (i=2;i<=n;i++)
	{
		if (array[i] < array[i-1])
		{
			array[0] = array[i];
			array[i] = array[i-1];
			for (j=i-2;array[0]< array[j];j--)
			{
				array[j+1] = array[j];
			}
			array[j+1] = array[0];
		}
	}
}

int main()
{
	int i;
	int *array;
	printf("请输入数组的大小：");
	scanf("%d",&n);
	array = (int*) malloc(sizeof(int) * (n+1));
	printf("请输入数组（用空格分隔）：");
	for (i=1;i<=n;i++)
	{
		scanf("%d",&array[i]);
	}
	InsertSort(array);
	printf("排序后为：");
	for (i=1;i<=n;i++)
	{
		printf("%d ",array[i]);
	}
	printf("\n");
}

