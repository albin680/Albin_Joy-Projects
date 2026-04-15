#include<stdio.h>
void main()
{
	int a[100],b[100],c[100],n,m,i,j,k,temp;
	printf("Enter the size of array 1 : ");
	scanf("%d",&n);
	printf("Enter the Array Elements : \n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Enter the size of array 2 : ");
	scanf("%d",&m);
	printf("Enter the Array Elements : \n");
	for(i=0;i<m;i++)
		scanf("%d",&b[i]);
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			if(a[i]>a[j]){
				temp=a[i];
				a[i]=a[j];
				a[j]=temp;
			}
		}
	}
	for(i=0;i<m;i++){
		for(j=i+1;j<m;j++){
			if(b[i]>b[j]){
				temp=b[i];
				b[i]=b[j];
				b[j]=temp;
			}
		}
	}
	i=j=0;
	while(i<m&&j<n)
	{
		if(a[i]<=b[j])
		{
			c[k]=a[i];
			i++;
			k++;
		}
		else
		{
			c[k]=b[j];
			j++;
			k++;
		}
	}
	while(i<m)
	{
		c[k]=a[i];
		k++;
		i++;
	}
	while(j<n)
	{
		c[k]=b[j];
		k++;
		j++;
	}
	printf("Array 1: ");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
	printf("\nArray 2: ");
	for(i=0;i<m;i++)
		printf("%d\t",b[i]);
	printf("\nMerged Array: ");
	for(i=0;i<m+n;i++)
		printf("%d\t",c[i]);
}
		
