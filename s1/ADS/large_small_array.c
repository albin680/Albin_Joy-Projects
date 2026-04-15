#include<stdio.h>
void main()
{
	int a[50],n,large=0,small,i;
	printf("Enter the size of the array: ");
	scanf("%d",&n);
	printf("Enter the elements in the array:\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("The array is : ");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
	small = a[0];
	for(i=0;i<n;i++){
		if(a[i]>large)
			large = a[i];
		if(a[i]<small)
			small = a[i];
	}
	printf("\n Largest Number is : %d",large);
	printf("\n Smallest Number is : %d",small);
}
