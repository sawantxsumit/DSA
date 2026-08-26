#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *head = NULL;
struct node *tail = NULL;
void addnode(int num)
{
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    newnode->data=num;
    if (head == NULL)
    {
        head = newnode;
        tail = newnode;
    }
    else
    {
        tail->next = newnode;
        tail=newnode;
    }
}
void displaylist()
{
    struct node * current=head;
    if(head==NULL)
    {
        printf("linked list is empty ");
    }
    int i=1;
    while(current != NULL)
    {
        printf("element %d = ",i);
        printf("%d\n", current->data);
        current=current->next;
    }
}
int main()
{
    int n,value;
    printf("enter the number of nodes :");
    scanf("%d", &n);
     
    //  printf("enter the value of the head node :");
    //  scanf("%d", &value);
    //  head->data=value;
    //  head->next=NULL;
    for (int i = 0; i < n; i++)
    {
        printf("enter the value for the %d node :", i+1);
        scanf("%d", &value);
        addnode(value);
    }

    displaylist();
    
    

    return 0;
}