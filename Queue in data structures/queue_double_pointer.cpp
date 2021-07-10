#include <iostream>
using namespace std;
class Queue
{
private:
int front;
int rear;
int size;
int *qu;
public:
Queue(){front=rear=-1;size=10;qu=new int[size];}
Queue(int size){front=rear=-1;
this -> size=size;qu=new int[this->size];}
void enqueue(int x);
int dequeue();
void Display();
};

void Queue::enqueue(int x)
{
if(rear==size-1)
printf("Queue Full\n");
else
{
rear++;
qu[rear]=x;
}
}

int Queue::dequeue()
{
int x=-1;
if(front==rear)
printf("Queue is Empty\n");
else

{
x=qu[front+1];
front++;
}
return x;
}

void Queue::Display()
{
printf("Vlaues present in queue are :- ");
for(int i=front+1;i<=rear;i++)
printf("%d ",qu[i]);
printf("\n\n");
}

int main()
{
Queue q(5);
q.enqueue(2);
q.enqueue(3);
q.enqueue(5);
q.Display();
q.dequeue();
q.Display();
return 0;
}