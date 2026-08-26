#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};
struct node *top;
int isEmpty(struct node *ptr)
{
    if (ptr == NULL)
    {
        return 1;
    }
    return 0;
}
// int isFull(struct node *ptr)
// {
    // struct node *p = (struct node *)malloc(sizeof(struct node));
//     if (ptr == NULL)
//     {
//         return 1;
//     }
//     return 0;
// }

void push(struct node *ptr, int num)
{
    // if (isFull(ptr) == 1)
    // {
    //     printf("stack overflow");
    // }
    struct node *n = (struct node *)malloc(sizeof(struct node));

    n->data = num;
    n->next = ptr;
    top = n;
}
// method --> 1
// void pop(struct node ** top)
// {
//     if (isEmpty(*top) == 1)
//     {
//         printf("stack underflow \n");
//         exit(0);
//     }
//     else
//     {
//         struct node *n=*top;
//         *top=(*top)->next;
//         int x= n->data;
//         free(n);
//         printf("the popped element is %d\n" , x);
//     }

// }

// method --> 2
void pop(struct node *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack underflow \n");
        exit(0);
    }
    else
    {
        struct node *n = ptr;
        top = ptr->next;
        int x = n->data;
        free(n);
        printf("the popped element is %d\n", x);
    }
}
void displayStack(struct node *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack is empty\n");
    }
    while (ptr != NULL)
    {
        printf("element = %d\n", ptr->data);
        ptr = ptr->next;
    }
}
int peek(struct node *ptr, int index)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack underflow \n");
        exit(0);
    }
    else
    {
        if (index > 5)
        {
            printf("invalid input !");
        }
        else
        {
        for (int i = 0; i < index && ptr != NULL; i++)
        {
            ptr = ptr->next;
        }
        int x = ptr->data;
        return x;
    }
    }
}

void topElement(struct node *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack uderflow ");
    }
    else
    {
        int x = ptr->data;
        printf("the top element is %d \n", x);
    }
}
void bottomElement(struct node *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack uderflow ");
    }
    else
    {
       for (int i = 0; ptr->next != NULL; i++)
        {
            ptr = ptr->next;
        }
        printf("the bottom element of the stack is %d \n" , ptr->data);
    }
}
int main()
{
     push(top, 70);
     push(top, 709);
     push(top, 74);
     push(top, 739);
     push(top, 79);
     push(top, 109);
    displayStack(top);

    pop(top);
    pop(top);

    displayStack(top);
    // int index;
    // printf("enter the index :");
    // scanf("%d", &index);
    // int x=  peek(top , index);
    // printf("the element at index %d is %d\n",index , x);
     

   // displayStack(top);
    topElement(top);
    bottomElement(top);
    return 0;
}