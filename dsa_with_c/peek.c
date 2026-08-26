#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
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
void push(int num, int top, struct stack *ptr)
{
    if (isFull(ptr) == 1)
    {
        printf("Stack overflow ");
        exit(0);
    }
    ptr->top++;
    ptr->arr[ptr->top] = num;
    printf("Element inserted\n");
}
void displayStack(struct stack *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack is empty\n");
    }
    for (int i = 0; i <= ptr->top; i++)
    {
        printf("index %d = %d \n", i ,ptr->arr[i]);
    }
}

int peek(struct stack *ptr, int index)
{
    if (index > ptr->top || index < 0)
    {
        printf("invalid value");
        exit(0);
    }
    int num;
    for (int i = 0; i <= index; i++)
    {
        num=ptr->arr[i];
    }
    
    return num;
}
int main()
{
    struct stack *s;
    s = (struct stack *)malloc(sizeof(struct stack));
    s->size = 80;
    s->top = -1;
    s->arr = (int *)malloc(s->size * sizeof(int));

    push(30, s->top, s);
    push(40, s->top, s);
    push(41, s->top, s);
    push(44, s->top, s);
    push(45, s->top, s);
    push(445, s->top, s);

    displayStack(s);
    int index;
    printf("enter the index :");
    scanf("%d", &index);
    printf("the element present at index %d is %d ", index, peek(s, index));
    return 0;
}