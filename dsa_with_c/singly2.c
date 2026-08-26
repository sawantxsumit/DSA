#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node* next;
};
struct node *head;
void displayLL(struct node *ptr)
{
    ptr=head;
    while(ptr != NULL)
    {
        printf("%d " , ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}
int main()
{
    int n , item ;
    printf("enter the number of nodes ");
    scanf("%d",&n);

    struct node  *p , *q;
    printf("enter the value of the head node :");
    scanf("%d",&item);

    q = (struct node*)malloc(sizeof(struct node));
    q->data=item;
    q->next=NULL;
    head=q;
    p=head;

    for (int i = 1; i < n; i++)
    {
        printf("enter the value of the next node :");
        scanf("%d",&item);

        q=(struct node *)malloc(sizeof(struct node));
        q->data=item;
        q->next = NULL;

        p->next=q;
        p=p->next;
        

    }
    
    displayLL(p);
return 0;
}