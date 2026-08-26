#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *head, *p,*temp;

void insertAtIndex(int index , int num)
{
    struct node *newnode , *temp ;
    newnode=(struct node *)malloc(sizeof(struct node));
    temp=head;
    int i=0;
    while(i<index-1)
    {
        temp=temp->next;
        i++;
    }

    newnode->data=num;
    newnode->next=temp->next;
    temp->next=newnode;
    printf("node inserted \n");
}
int main()
{
    int n, item;
    printf("enter the number of nodes :");
    scanf("%d", &n);

    struct node *q;
    printf("enter the value of the head node :");
    scanf("%d", &item);

    q = (struct node *)malloc(sizeof(struct node));
    q->data = item;
    q->next = NULL;
    head = q;
    p = head;

    for (int i = 1; i < n; i++)
    {
        printf("enter the value of the next node :");
        scanf("%d", &item);
        q = (struct node *)malloc(sizeof(struct node));

        q->data = item;
        q->next = NULL;

        p->next = q;
        p = p->next;
    }

    printf("the original linked list is :\n");
    p = head;
    while (p != NULL)
    {
        printf("%d\t", p->data);
        p = p->next;
    }

    //inserting at given index
    int index;
    printf("\nenter the index where you want to insert the node :");
    scanf("%d", &index);

    if(index > n) 
    {
        printf("invalid input ");
        exit(0);
    }
    printf("enter the value of the new node :");
    scanf("%d", &item);

    insertAtIndex(index,item);

    //printing the updated linked list
    printf("the new linked list is :\n");
    p = head;
    while (p != NULL)
    {
        printf("%d\t", p->data);
        p = p->next;
    }
return 0;
}