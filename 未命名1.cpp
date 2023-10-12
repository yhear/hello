#include<stdio.h>
#define pi 3.14
#define C 2*pi*r
int main(void)
{
	double r,h,S,T;
	printf("r的值:");
	scanf("%lf",&r);
	printf("h的值:");
	scanf("%lf",&h);
 	S=pi*r*r;
 	T=4/3*pi*r*r;
 	printf("圆的周长:%.3f\n",C);
	 printf("圆的面积:%.3f\n",S);
	 printf("圆球的表面积:%.3f\n",4*pi*r*r);
	 printf("圆球的体积:%.3f\n",T);
	 printf("圆柱的体积:%.3f\n",S*h);
	 return(0);
	  
}