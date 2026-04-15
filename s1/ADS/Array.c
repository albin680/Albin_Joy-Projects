#include<stdio.h>
void main()
{
	int m,n,a[10],b[10],c[20],i,j,t,k=0;
	printf("Enter size of array a:\n");
	scanf("%d",&m);
	printf("Enter array elements:\n");
	for(i=0;i<m;i++)
		scanf("%d",&a[i]);
	printf("Enter size of array b:\n");
	scanf("%d",&n);
	printf("Enter array elements:\n");
	for(i=0;i<n;i++)
		scanf("%d",&b[i]);
	for(i=0;i<m;i++)
		for(j=i+1;j<m;j++)
			if(a[i]>a[j])
			{
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
			if(b[i]>b[j])
			{
				t=b[i];
				b[i]=b[j];
				b[j]=t;
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
	printf("\nArray a:\n");
	for(i=0;i<m;i++)
		printf("%d\t",a[i]);
	printf("\nArray b:\n");
	for(i=0;i<n;i++)
		printf("%d\t",b[i]);
	printf("\nArray c:\n");
	for(i=0;i<m+n;i++)
		printf("%d\t",c[i]);
}
