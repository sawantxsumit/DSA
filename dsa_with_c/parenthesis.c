#include <stdio.h>
#include <stdlib.h>

// this program is made for parenthesis matching problem
struct stack
{
    int size;
    int top;
    char *arr;
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

void push(char val, struct stack *ptr)
{
    if (isFull(ptr) == 1)
    {
        printf("Stack overflow ");
        exit(0);
    }
    ptr->top++;
    ptr->arr[ptr->top] = val;
    // printf("Element inserted\n");
}

char pop(int top, struct stack *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("Stack underflow ");
        return 0;
    }
    char val = (ptr->arr[ptr->top]);
    ptr->top--;
    return val;
}

void displayStack(struct stack *ptr)
{
    if (isEmpty(ptr) == 1)
    {
        printf("stack is empty\n");
    }
    for (int i = 0; i <= ptr->top; i++)
    {
        printf("Index %d = %d \n", i, ptr->arr[i]);
    }
}

int parenthesisMatch(char *exp)
{
    // create and intialize stack
    struct stack *sp;
    sp->size = 100; // size can be varied and taken as an argument
    sp->top = -1;
    sp->arr = (char *)malloc(sp->size * sizeof(char));
    for (int i = 0; i < exp[i] != '\0'; i++)
    {
        if (exp[i] == '(')
        {
            push('(', sp);
        }
        else if (exp[i] == ')')
        {
            // if the stack is empty and a right parenthesis is found then the parenthesis are not matching
            if (isEmpty(sp) == 1)
            {
                return 0;
            }
            pop(')', sp);
        }
    }

    if (isEmpty(sp) == 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main()
{
    char exp[] = "8*7(9 - 4)";
    if (parenthesisMatch(exp) == 1)
    {
        printf("the parenthesis is matching ");
    }
    else
    {
        printf("the parenthesis is  not matching ");
    }

    return 0;
}