#include<stdio.h>
#include<stdlib.h>
struct node{
  int info;
  struct node *link;
};
struct node *start=NULL;
void traverse();
void insertAtFront();
void insertAtEnd();
void insertAtPosition();
void deleteFirst();
void deleteEnd();
void deletePosition();
void search();
void main(){
 int ch;
 while(1){
   printf("\n1.See List\n2.Insertion at Starting\n3.Insertion at end\n4.Insertion at any position\n5.Delete First Element\n6.Delete Last Element\n7.Delete Element at any position\n8.Search\n9.Exit\n");
   printf("\nEnter Your Choice:\n");
   scanf("%d",&ch);
   switch(ch){
     case 1:traverse();
            break;
     case 2:insertAtFront();
            break;
     case 3:insertAtEnd();
            break;
     case 4:insertAtPosition();
            break;
     case 5:deleteFirst();
            break;
     case 6:deleteEnd();
            break;
     case 7:deletePosition();
            break;
     case 8:search();
            break;
     case 9:exit(0);
     default:printf("\nEnter valid choice\n");
     }
 }
}
void traverse(){
  struct node *temp;
  if(start==NULL)
    printf("List is Empty\n");
  else{
    temp=start;
    printf("the list is\n");
    while(temp!=NULL){
      printf("%d-->",temp->info);
      temp=temp->link;
       }
   }
}
void insertAtFront(){
  int data;
  struct node *temp;
  temp=malloc(sizeof(struct node));
  printf("Enter the number to be inserted:\n");
  scanf("%d",&data);
  temp->info=data;
  temp->link=start;
  start=temp;
}
void insertAtEnd(){
  int data;
  struct node *temp,*head;
  temp=malloc(sizeof(struct node));
  printf("Enter the number to be inserted:\n");
  scanf("%d",&data);
  temp->link=0;
  temp->info=data;
  head=start;
  while(head->link!=NULL)
  {
    head=head->link;
  }
  head->link=temp;
}
void insertAtPosition(){
  struct node *temp,*newnode;
  int pos,data,i=1;
  newnode=malloc(sizeof(struct node));
  printf("Enter Position & Data:\n");
  scanf("%d%d",&pos,&data);
  temp=start;
  newnode->info=data;
  newnode->link=0;
  while(i<pos-1){
    temp=temp->link;
    i++;
    }
  newnode->link=temp->link;
  temp->link=newnode;
}
void deleteFirst(){
  struct node *temp;
  if(start==NULL)
    printf("\nList is empty\n");
  else{
    temp=start;
    start=start->link;
    free(temp);
    }
}
void deleteEnd(){
  struct node *temp,*prevnode;
  if(start==NULL)
    printf("\nList is Empty\n");
  else{
    temp=start;
    while(temp->link!=0)
      {
       prevnode=temp;
       temp=temp->link;
      }
    free(temp);
    prevnode->link=0;
  }
}
void deletePosition(){
  struct node *temp,*position;
  int i=1,pos;
  if(start==NULL)
    printf("\nList is Empty\n");
  else{
    printf("Enter the position\n");
    scanf("%d",&pos);
    position=malloc(sizeof(struct node));
    temp=start;
    while(i<pos-1)
    {
      temp=temp->link;
      i++;
     }
  position=temp->link;
  temp->link=position->link;
  free(position);
  }
}
void search(){
  int found=-1,key;
  struct node *tr=start;
  if(start==NULL)
  {
    printf("Linked list is empty\n");
  }
  else
  {
    printf("\nEnter the element you want:");
    scanf("%d",&key);
    while(tr!=NULL)
    {
      if(tr->info==key)
      {
        found=1;
        break;
      }
      else
      {
        tr=tr->link;
      }
    }
    if(found==1)
    {
      printf("%d is present in the linked list\n",key);
    }
    else{
      printf("%d is not present in the linked list\n",key);
    }
  } 
}
