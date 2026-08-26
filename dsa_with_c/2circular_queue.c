#include <stdio.h>
#include <stdlib.h>

struct circularQueue
{
    int size;
    int front;
    int rear;
    int *arr;
};

int isFull(struct circularQueue *q)
{
    if ((q->rear + 1) % q->size == q->front)
    {
        return 1;
    }
    return 0;
}
int isEmpty(struct circularQueue *q)
{
    if (q->front == q->rear)
    {
        return 1;
    }
    return 0;
}
void enqueue(struct circularQueue *q, int val)
{
    if (isFull(q))
    {
        printf("circularQueue overflow \n");
    }
    else
    {
        q->rear = (q->rear + 1) % q->size;
        q->arr[q->rear] = val;
        printf("enqueue\n");
    }
}
void dequeue(struct circularQueue *q)
{
    int a = -1;
    if (isEmpty(q))
    {
        printf("circularQueue underflow \n");
        return;
    }
    else
    {
        q->front = (q->front + 1) % q->size;
        a = q->arr[q->front];
    }
    printf("the dequeued element is : %d\n", a);
}

void display(struct circularQueue *q)
{
    if (isEmpty(q))
    {
        printf("circularQueue  underflow \n");
    }
    else
    {
        for (int i = q->front + 1; i <= q->rear; i++)
        {
            printf("%d ", q->arr[i]);
        }
        printf("\n");
    }
}

int main()
{
    struct circularQueue  p;
    p.size = 6;
    p.front = p.rear = 0;
    p.arr = (int *)malloc(p.size * sizeof(int));
   

   // for a circular queue of size 6 we can only insert 5 values as one postion is reserved for front
    enqueue(&p, 99);
    enqueue(&p, 93);
    enqueue(&p, 55);
    enqueue(&p, 66);
    enqueue(&p, 45);
    printf("original circularQueue :\n");
    display(&p);
     
    dequeue(&p); 
    dequeue(&p); 
    dequeue(&p); 
    dequeue(&p); 
    dequeue(&p); 
    
    enqueue(&p, 43);
    enqueue(&p, 4);
    enqueue(&p, 48);
    

    display(&p);//not working
    
    return 0;
}