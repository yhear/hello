#include<stdio.h> 
int main(void)
{
	int x,y;
	printf("你的年龄：");
	scanf("%d",&x);
	y=365*x;
	printf("你的天数：%d\n",y); 
	return 0;
} 