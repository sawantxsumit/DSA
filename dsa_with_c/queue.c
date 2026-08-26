#include <stdio.h>
#include <stdlib.h>
struct queue
{
    int size;
    int front;
    int rear;
    int *arr;
};

int isFull(struct queue *q)
{
    if (q->rear == q->size - 1)
    {
        return 1;
    }
    return 0;
}
int isEmpty(struct queue *q)
{
    if (q->front == q->rear)
    {
        return 1;
    }
    return 0;
}
void enqueue(struct queue *q, int val)
{
    if (isFull(q))
    {
        printf("queue overflow \n");
    }
    else
    {
        q->rear++;
        q->arr[q->rear] = val;
    }
}
void dequeue(struct queue *q)
{
    int a = -1;
    if (isEmpty(q))
    {
        printf("queue underflow \n");
        return;f
    }
    else
    {
        q->front++;
        a = q->arr[q->front];
    }
    printf("the dequeued element is : %d\n", a);
}

void display(struct queue *q)
{
    if (isEmpty(q))
    {
        printf("queue underflow \n");
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
    struct queue p;
    p.size = 10;
    p.front = p.rear = -1;
    p.arr = (int *)malloc(p.size * sizeof(int));

    enqueue(&p, 99);
    enqueue(&p, 93);
    enqueue(&p, 55);
    enqueue(&p, 66);
    enqueue(&p, 45);
    enqueue(&p, 23);
    printf("original queue :\n");
    display(&p);

    dequeue(&p);
    dequeue(&p);
    printf("updated queue is :\n");
    display(&p);
    return 0;
}