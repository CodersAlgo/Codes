#include <stdio.h>
#include <stdlib.h>

struct Stack
{
int size;
int top;
int *S;
};

void create(struct Stack *st,int sizee)
{
st->size = sizee;
st->top=-1;
st->S=(int *)malloc(st->size*sizeof(int));
}

void Display(struct Stack st)
{
int i;
printf("values present in stack are :- ");
for(i=st.top;i>=0;i--)
printf("%d \t",st.S[i]);
printf("\n");
}

void push(struct Stack *st,int x)
{
if(st->top==st->size-1)
printf("Stack overflow\n");
else
{
st->top++;
st->S[st->top]=x;
}

}

int pop(struct Stack *st)
{
int x=-1;
if(st->top==-1)
printf("Stack Underflow\n");
else
{
x=st->S[st->top--];
}
return x;
}

int peek(struct Stack st,int index)
{
int x=-1;
if(st.top-index+1<0)
printf("Invalid Index \n");
x=st.S[st.top-index+1];
return x;
}

int isEmpty(struct Stack st)
{
if(st.top==-1)
return 1;
return 0;
}

int isFull(struct Stack st)
{
return st.top==st.size-1;
}

int stackTop(struct Stack st)
{
if(!isEmpty(st))

return st.S[st.top];
return -1;
}

int main()
{
struct Stack st;
int size,d;
printf("Enter the size of stack :- ");
scanf("%d",&size);
create(&st,size);
// Insert the elements into stack by calling push 
push(&st,9);
push(&st,6);
push(&st,8);
push(&st,1);
printf("Top element present in stack is :- %d \n",peek(st,1));
//Get the Top most element of stack using the peek
Display(st);
//display function displays all elements present in the stack
d = pop(&st);
// pops out the top most element present in stack
printf("popped out %d from stack\n",d);
Display(st);
return 0;
}