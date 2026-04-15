#include<stdio.h>
int main()
{
int numbers[10];
printf("enter 10 numbers\n");
for(int i=0;i<10; i++)
{
printf("enter number %d:",i+1);
scanf("%d",&numbers[i]);
}
printf("the entered numbers are:\n");
for(int i=0;i<10;i++)
{
printf("%d\n",numbers[i]);
}
return 0;
}
