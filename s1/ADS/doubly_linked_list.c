#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
struct node{
  int data;
  struct node *prev;
  struct node *next;
};
struct node *start;
void display();
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
   printf("\n1.Display\n2.Insertion at Starting\n3.Insertion at end\n4.Insertion at any position\n5.Delete First Element\n6.Delete Last Element\n7.Delete Element at any position\n8.Search\n9.Exit\n");
   printf("\nEnter Your Choice:\n");
   scanf("%d",&ch);
   switch(ch){
     case 1:display();
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
void display(){
  struct node *ptr;
  ptr=start;
  if(ptr==NULL)
    printf("\nList is empty");
  else{
    while(ptr!=NULL)
    {
      printf("%d->",ptr->data);
      ptr=ptr->next;
    }
    printf("null");
  }
}
void insertAtFront(){
  struct node *ptr;
  int x;
  ptr=(struct node*)malloc(sizeof(struct node*));
  if(ptr==NULL)
    printf("\nOverflow");
  else{
    printf("\nEnter value: ");
    scanf("%d",&x);
    if(start==NULL)
    {
      ptr->data=x;
      ptr->prev=NULL;
      ptr->next=NULL;
      start=ptr;
    }else{
      ptr->data=x;
      ptr->prev=NULL;
      ptr->next=start;
      start->prev=ptr;
      start=ptr;
    }
  }
}
void insertAtEnd(){
  struct node *ptr,*temp;
  int x;
  ptr=(struct node*)malloc(sizeof(struct node*));
  if(ptr==NULL)
    printf("\nOverflow");
  else{
    printf("\nEnter value: ");
    scanf("%d",&x);
    ptr->data=x;
    if(start==NULL)
    {
      ptr->next=NULL;
      ptr->prev=NULL;
      start=ptr;
    }else{
      temp=start;
      while(temp->next!=NULL){
        temp=temp->next;
      }
      temp->next=ptr;
      ptr->prev=temp;
      ptr->next=NULL;
    }
  }    
}
void insertAtPosition(){
  int pos,i,x;
  struct node *ptr,*temp;
  ptr=(struct node*)malloc(sizeof(struct node*));
  if(ptr==NULL)
    printf("\nOverflow");
  else{
    printf("\nEnter value: ");
    scanf("%d",&x);
    ptr->data=x;
    printf("\nEnter the position: ");
    scanf("%d",&pos);
    temp=start;
    if(pos==1)
    {
      if(start==NULL){
        ptr->data=x;
        ptr->prev=NULL;
        ptr->next=NULL;
        start=ptr;
      }else{
        ptr->data=x;
        ptr->prev=NULL;
        ptr->next=start;
        start->prev=ptr;
        start=ptr;
      }
    }else{
      for(i=1;i<pos-1;i++)
      {
        temp=temp->next;
        if(temp==NULL)
          printf("\nCan't insert");
      }
      ptr->next=temp->next;
      temp->next=ptr;
      ptr->prev=temp;
      if(temp==NULL){
        printf("\nCan't insert");
        return;
      }
    }
  }
}
void deleteFirst(){
  int x;
  struct node *ptr;
  if(start==NULL)
    printf("\nList is empty");
  else{
    ptr=start;
    start=ptr->next;
    start->prev=NULL;
    x=ptr->data;
    free(ptr);
    printf("\n%d deleted",x);
  }
}
void deleteEnd(){
  int x;
  struct node *ptr,*ptr1;
  if(start==NULL)
    printf("\nList is empty");
  else if(start->next==NULL)
  {
    x=start->data;
    start=NULL;
    free(start);
    printf("\n%d deleted",x);
  }else{
    ptr=start;
    while(ptr->next!=NULL){
      ptr1=ptr;
      ptr=ptr->next;
    }
    ptr->next=NULL;
    ptr->prev=NULL;
    x=ptr->data;
    free(ptr);
    printf("\n%d deleted",x);
  }
}
void deletePosition(){
  struct node *ptr,*ptr1;
  int pos,i,x;
  ptr=start;
  if(ptr==NULL)
    printf("\nList is empty");
  else{
    printf("\nEnter the position: ");
    scanf("%d",&pos);
    if(pos==1){
      ptr=start;
      start=ptr->next;
      start->prev=NULL;
      x=ptr->data;
      free(ptr);
      printf("\n%d deleted",x);
    }else{
      for(i=1;i<pos;i++){
        ptr1=ptr;
        ptr=ptr->next;
        if(ptr==NULL){
          printf("\nCan't delete");
          return;
        }
      }
      ptr1->next=ptr->next;
      (ptr->next)->prev=ptr1;
      x=ptr->data;
      free(ptr);
      printf("\n%d deleted",x);
    }
  }
}
void search(){
  struct node *ptr;
  int x,i=0,f;
  ptr=start;
  if(ptr==NULL)
    printf("\nList is empty");
  else{
    printf("\nEnter element to search: ");
    scanf("%d",&x);
    while(ptr!=NULL){
      if(ptr->data=x){
        printf("\nItem found at position %d",i+1);
        f=0;
        break;
      }else
        f=1;
      i++;
      ptr=ptr->next;
    }
    if(f==1)
      printf("\nItem not found");
  }
}
