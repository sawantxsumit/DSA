#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *head;
    struct node *p, *q;

void displayLL(struct node *ptr)
{
    ptr = head;
    while (ptr != NULL)
    {
        printf("%d\t", ptr->data);
        ptr = ptr->next;
    }
}

void delete(struct node *ptr , int pos)
{
    if (pos==1) //because the code in "else" does'nt work for first position
{
    p=head;
    head=head->next;
    free(p);
     
    displayLL(p);
}
else
{
struct node *w=head;
struct node *s=head;

for (int i = 1; i < pos-1; i++)
{
    w=w->next;
    s=s->next;
}

w=w->next;
s->next=w->next;

free(w);
displayLL(s);
}
}
int main()
{
    int n, item;
    printf("enter the number of nodes :");
    scanf("%d", &n);

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

    displayLL(p);

    // deletion in linked list
    // printf("\ncase 1-> deleting first element \n");
    
    // p=head;
    // head=head->next;
    // free(p);
     
    // displayLL(p);

//     printf("\ncase 2-> deleting the last element \n");
   
//    struct node *w=head;
//     for (int i = 1; i < n-1; i++)
//     {
//         w=w->next;
//     }
     
//      p=w->next;
//      w->next=NULL;
//      free(p);
     
//      displayLL(w);

printf("\n Deleting a node at given position \n");

int pos;
printf("enter the position of the element to delete :");
scanf("%d", &pos);

delete(p,pos);
   return 0;
}