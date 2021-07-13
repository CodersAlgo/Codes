#include <stdio.h>
#include <stdlib.h>

struct Queue
{
int size;
int front;
int rear;
int *Q;
};

void create(struct Queue *q,int size)
{
q->size=size+1;
q->front=q->rear=0;
q->Q=(int *)malloc(q->size*sizeof(int));
}

void enqueue(struct Queue *q,int x)
{

if((q->rear+1)%q->size==q->front)
printf("Queue is full cannot enqueue the element\n");

else
{
q->rear=(q->rear+1)%q->size;
q->Q[q->rear]=x;
}

}

int dequeue(struct Queue *q)
{
int x=-1;

if(q->front==q->rear)
printf("Queue is empty cannot dequeue the element\n");

else
{
q->front=(q->front+1)%q->size;
x=q->Q[q->front];
printf("%d dequeued\n",x);
}

return x;
}

void print_queue(struct Queue q)
{
int i=q.front+1;
printf("\nPrinting elements of queue :- \n");
do
{
printf("%d \t",q.Q[i]);
i=(i+1)%q.size;
}while(i!=(q.rear+1)%q.size);

printf("\n\n");
}

int main()
{

// creating a circular queue of size 5
struct Queue q;
create(&q,5);

// inserting 5 elements into the circular queue
enqueue(&q,2);
enqueue(&q,3);
enqueue(&q,7);
enqueue(&q,0);
enqueue(&q,1);
print_queue(q);

// Trying to insert 6 th element
enqueue(&q,5);

// dequeuing two elements for space 
dequeue(&q);
dequeue(&q);

// Inserting new elements in free space 
enqueue(&q,5);
enqueue(&q,6);

// printing values present in queue after insertion
print_queue(q);
printf("\n");

return 0;
}