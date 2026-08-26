#include <stdio.h>
#include <stdlib.h>
#define MAX 500

//this program includes :-
//push()
//pop()
//traverseing the stack using array
//displaystack()
struct stack
{
    int size ;
    int top;
    int arr[MAX];
};

int isEmpty(struct stack *ptr)
{
    if (ptr->top == -1)
    {
        return 1;
    }
    return 0;
}
int isFull(struct stack *ptr)
{
    if (ptr->top == ptr->size - 1)
    {
        return 1;
    }
    return 0;
}

void push(int num, struct stack *ptr)
{
    if (isFull(ptr) == 1)
    {
        printf("Stack overflow ");
        exit(0);
    }
    ptr->top++;
    ptr->arr[ptr->top] = num;
   // printf("Element inserted\n");
}

int pop(int top, struct stack *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("Stack underflow "); 
        return 0;
    }
    int num = (ptr->arr[ptr->top]);
    ptr->top--;
    return num;
}

void displayStack(struct stack *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack is empty\n");
    }
  for (int i = 0; i <= ptr->top; i++)
    {
    printf("Index %d = %d \n",i, ptr->arr[i]);    
    }   
}
int main()
{
    
    struct stack *s;
    s=(struct stack *)malloc(sizeof(struct stack));
    s->size = 80;
    s->top = -1;
  //  s->arr = (int *)malloc(s->size * sizeof(int));

    push(30, s);
    push(40, s);
    push(41, s);
    push(44, s);
    push(45, s);
    push(445, s);
    
    displayStack(s);

    printf("element %d is popped from the stack \n", pop(s->top,s));
    printf("stack after popping :\n");
    displayStack(s);
    free(s->arr);
 
    return 0;
}