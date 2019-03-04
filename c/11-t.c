#include<stdio.h>
#define N 100

int main()
{
	int a[N] = {0}, i = 0, out = 0, num = 0, *p;
	p = a;
	while (1){
		if (*p==0){
			if (out == (N-1)) break;
			num++;
			num = num % 3;
			if (num == 0){
				*p = 1;
				out++;}
		}
		p++;
		if (p == a+N)
			p = a;
	}
	printf("最后剩余者的编号是：%ld\n", p + 1 -a);
	return 0;
}
