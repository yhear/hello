#include<stdio.h>
#define pi 3.14
#define C 2*pi*r
int main(void)
{
	double r,h,S,T;
	printf("r��ֵ:");
	scanf("%lf",&r);
	printf("h��ֵ:");
	scanf("%lf",&h);
 	S=pi*r*r;
 	T=4/3*pi*r*r;
 	printf("Բ���ܳ�:%.3f\n",C);
	 printf("Բ�����:%.3f\n",S);
	 printf("Բ��ı����:%.3f\n",4*pi*r*r);
	 printf("Բ������:%.3f\n",T);
	 printf("Բ�������:%.3f\n",S*h);
	 return(0);
	  
}