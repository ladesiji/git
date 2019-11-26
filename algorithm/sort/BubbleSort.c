#include <stdio.h>
#include <stdlib.h>

int n;

/*
 *冒泡排序
 */
void BubbleSort(int *array)
{
	int i,j,temp;
	for (i=0;i<n-1;i++)
	{
		for(j=0;j<n-1-i;j++)
		{
			if(array[j]>array[j+1])
			{
				temp = array[j];
				array[j] = array [j+1];
				array[j+1] = temp;
			}
		}
	}
}

int main()
{
	int i;
	int *array;
	printf("请输入数组大小：");
	scanf("%d",&n);
	array = (int*) malloc(sizeof(int)*n);
	printf("请输入数据（用空格隔开）：");
	for (i=0;i<n;i++)
	{
		scanf("%d",&array[i]);
	}
	BubbleSort(array);
	printf("排序后为：");
	for (i=0;i<n;i++)
	{
		printf("%d ",array[i]);
	}
	printf("\n");
}
