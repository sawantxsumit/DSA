#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
};

void lltraverse (struct node *ptr)
{
    while(ptr != NULL)
    {
    printf(" Element %d \n",ptr->data);
    ptr=ptr->next;
    }
}
int main()
{
    int n , item;
    struct node * head ;
    struct node * second ;
    struct node * third;
    struct node * ptr;

    //allocate memeory for nodes in the linked list in heap
    head = (struct node * )malloc(sizeof(struct node));
    second = (struct node * )malloc(sizeof(struct node));
    third = (struct node * )malloc(sizeof(struct node));
    
    //head node
    printf("enter value for the head node :");
    scanf("%d",&item );
    head->data=item;
    head->next=second;
    //second node
        printf("enter the value of the next node");
        scanf("%d", &item);
        second->data=item;
        second->next=third;

     //third node   
        printf("enter the value of the next node");
        scanf("%d", &item);
        third->data=item;
        third->next=NULL;

    //printing the linked list
    ptr=head;
     while(ptr != NULL)
    {
    printf(" Element %d \n",ptr->data);
    ptr=ptr->next;
    }
return 0;
}