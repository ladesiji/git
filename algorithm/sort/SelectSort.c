#include<stdio.h>
#include<stdlib.h>

int n;

/*
 * 选择排序
 */
void SelectSort(int *array)
{
	int i, j, k, temp;
	for (i=0;i<n;i++)
	{
		k = i;
		for (j=i+1;j<n;j++)
		{
			if(array[j]<array[k])
			{
				k = j;
			}
		}
		if (k != i)
		{
			temp = array[i];
			array[i] = array[k];
			array[k] = temp;
		}
	}
}

int main()
{
	int i;
	int *array;
	printf("请输入数组大小：");
	scanf("%d", &n);
	array = (int*) malloc(sizeof(int) * n);
	printf("请输入数据（用空格分隔）：");
	for (i=0;i<n;i++)
	{
		scanf("%d", &array[i]);
	}
	SelectSort(array);
	printf("排序后为：");
	for (i=0;i<n;i++)
	{
		printf("%d ", array[i]);
	}
	printf("\n");
}
