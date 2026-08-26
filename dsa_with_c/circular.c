#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *head;
void displayCLL(struct node *ptr)
{
     ptr=head;
    do
    {
        printf("%d\n", ptr->data);
        ptr=ptr->next;
    }
    while(ptr != head);
}

int main()
{
    int n, item;
    printf("enter the number of nodes :");
    scanf("%d", &n);

    struct node *p, *q;
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
        
        q=(struct node *)malloc(sizeof(struct node));
        q->data = item;
        q->next = NULL;

        p->next = q;
        p = p->next;
    }
    
    p->next=head; //linking the last node to the head node

    displayCLL(p);
    
    return 0;
}