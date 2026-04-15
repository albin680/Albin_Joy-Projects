#include<stdio.h>
#include<stdlib.h>
int a[50],front=-1,rear=-1,n;
void enqueue(){
	int value;
	if((front==0&&rear==n-1)||(front==rear+1))
		printf("Queue is full");
	else{
		printf("Enter the value to be inserted: ");
		scanf("%d",&value);
		if(front==-1&&rear==-1)
			front=rear=0;
		else if(rear==n-1&&front!=0)
			rear=0;
		else
			rear=rear+1;
		a[rear]=value;
	}
}
void dequeue(){
	if(front==-1)
		printf("Queue is Empty");
	else{
		printf("%d is deleated",a[front]);
		if(front==rear)
			front=rear=-1;
		else
			front=(front+1)%n;
	}
}
void display(){
	int i;
	if(front==-1)
		printf("Queue is Empty");
	else{
		if(front<=rear){
			for(i=front;i<=rear;i++)
				printf("%d\t",a[i]);
		}else{
			for(i=front;i<n;i++)
				printf("%d\t",a[i]);
			for(i=0;i<=rear;i++)
				printf("%d\t",a[i]);
		}
	}
}
void search(){
	int value,i,j,f1,f2;
	if(front==-1)
		printf("Queue is Empty");
	else{
		printf("Enter the element to be searched: ");
		scanf("%d",&value);
		if(front<=rear){
			f1=0;
			for(i=front,j=0;i<=rear;i++,j++){
				if(a[i]==value){
					printf("%d found at the position %d",value,j);
					f1=1;
					break;
				}
			}
			if(f1==0)
				printf("Element not found");
		}else{
			f2=0;
			for(i=front,j=0;i<n;i++,j++){
				if(a[i]==value){
					printf("%d found at the position %d",value,j);
					f2=1;
					break;
				}
			}
			if(f2==0){
				for(i=0,j=j;i<=rear;i++,j++){
					if(a[i]==value){
						printf("%d found at the position %d",value,j);
						f2=1;
						break;
					}
				}
			}
			if(f2==0){
				printf("Element not found");
			}
		}
	}
}
void main()
{
	int ch;
	printf("Enter the size of the queue: ");
	scanf("%d",&n);
	while(1){
		printf("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Search\n5.Exit\n");
		printf("Enter Your Choice: ");
		scanf("%d",&ch);
		switch(ch){
			case 1:	
				enqueue();
				break;
			case 2:
				dequeue();
				break;
			case 3:
				display();
				break;
			case 4:
				search();
				break;
			case 5:
				exit(0);
			default:
				printf("Enter a valid choice");
		}
	}
}
