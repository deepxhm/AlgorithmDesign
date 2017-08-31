#include<stdio.h>
struct bs
{

unsigned char a:4;
unsigned char b:4;
} i; 

int main(void)
{
//printf("Hello,world\n");
for(i.a=1;i.a<=9;i.a++)
	for(i.b=1;i.b<=9;i.b++)
		if(i.a%3 !=i.b%3)
			printf("A=%d,b=%d\n",i.a,i.b);
return 0;
}
/*
使用位域，解决中国象棋将帅问题。

gcc ChessPuzzle.cpp -o ChessPuzzle
./ChessPuzzle

*/
