#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head, *p,*temp;

void insertAtFirst(int num)
{
    p = (struct node *)malloc(sizeof(struct node));
    p->data = num;
    p->next = head;

    head = p;
    printf("node inserted ");
}

    
void insertAtEnd(int num)
{
    struct node * newnode , *temp;
    newnode=(struct node *)malloc(sizeof(struct node));
    temp=head;
    while(temp->next != NULL)
    {
        temp=temp->next;
    }
    temp->next=newnode;
    newnode->data=num;
    newnode->next=NULL;
    printf("node inserted\n ");

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
    
    //inserting at beginning
    printf("\nEnter the item which you want to insert at beginning :");
    scanf("%d", &item);
    insertAtFirst(item);
    
    //inserting at last
    printf("\nEnter the item which you want to insert at end :");
    scanf("%d", &item);
    insertAtEnd(item);
 
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