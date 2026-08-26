#include <stdio.h>
#include <time.h>
#include <conio.h>e 
#include <stdlib.h>
#define MAX 6
int queue[MAX];

int front = -1;
int rear = -1;

void enqueue();
void dequeue();
void display();

int main()
{
    int choice = 1, x;
    while (choice < 4 && choice != 0)
    {
        printf("\n press 1 : insert an element \n");
        printf("\n press 2 : delete an element \n");
        printf("\n press 3 : display the elements \n");
        printf("\n press 4 : quit \n");
        printf("\nenter your choice :");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("enter the element to be inserted :");
            scanf("%d", &x);
            enqueue(x);
            break;
        case 2:
            dequeue();
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
        default:
            break;
        }
    }
    return 0;
}

void enqueue(int element)
{
    if (front == -1 && rear == -1) // for empty
    {
        front = 0;
        rear = 0;
        queue[rear] = element;
    }
    else if ((rear + 1) % MAX == front) // for full
    {
        printf("queue overflow ");
    }
    else
    {
        rear = (rear + 1) % MAX;
        queue[rear] = element;
    }
}

void dequeue()
{
    if (front == -1 && rear == -1) // for empty
    {
        printf("queue underflow ");
    }
    else if (front == rear)
    {
        printf("the dequeued element is %d ", queue[front]);
        front = -1;
        rear = -1;
    }
    else
    {
        printf("the dequeued element is %d", queue[front]);
        front = (front + 1) % MAX;
    }
}

void display()
{
    int i = front;
    if (front == -1 && rear == -1) // for empty
    {
        printf("queue is empty ");
    }
    else
    {
        printf("\n Elements in the queue are :\n");
        while (i <= rear)
        {
            printf("%d ", queue[i]);
            i = (i + 1) % MAX;
        }
    }
}