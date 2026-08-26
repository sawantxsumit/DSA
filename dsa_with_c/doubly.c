#include<stdio.h>
#include<stdlib.h>

struct node 
{
    int data;
    struct node * prev;
    struct node * next;
};

struct node *head;
int main()
{
    int item,n;
    struct node *p , *q;
    printf("enter the  number of nodes :");
    scanf("%d", &n);
    printf("enter the value of head node :");
    scanf("%d", &item);
    q=(struct node*)malloc(sizeof(struct node));
    q->prev= NULL;
    q->data=item;
    q->next=NULL;
    head=q;
    p=head;
    for (int i = 1; i < n; i++)
    {
        printf("enter the value of the next node :");
        scanf("%d", &item);
        q=(struct node*)malloc(sizeof(struct node));
        q->prev=p;
        q->data=item;
        q->next=NULL;

        p->next=q;
        p=p->next;
    }
    
    printf("the doubly linked list is :\n");
    p=head;
    while(p != NULL)
    {
        printf("%d\t", p->data);
        p=p->next;
    }
return 0;
}