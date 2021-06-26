import numpy as np
 
class stack() :

    def __init__(self,size) :
        self.size = size
        self.arr = np.array([None]*self.size)
        self.top = -1

    def push(self,value) :
        if self.top < self.size :
            self.top += 1
            self.arr[self.top] = value
        else :
            print("\nStack overflow \n")

    def pop(self) :
        if self.top == -1 :
            print("\nStack underflow \n")
        else :
            self.top -= 1
            return self.arr[self.top+1]

    def peek(self) :
        if self.top == -1 :
            print("\nStack underflow \n")
        else :
            return "\nTop element present in stack is :-  "+str(self.arr[self.top])+" \n"

    def isempty(self) :
        if self.top == -1 :
            return "\nStack is empty \n"
        else :
            return "\nStack is not empty \n"

    def isfull(self) :
        if self.top == self.size - 1 :
            return "\nStack is full \n"
        else :
            return "\nStack is not full \n"

    def display(self) :
        if self.top == -1 :
            print("\nStack underflow \n")
        else :
            print("\nValues present in stack are :- \n")
            for x in range(self.top+1) :
                print(self.arr[x],end="\t")
            print("\n")
        
s = stack(5)
a = [9,6,8,1]

for x in a :
    s.push(x)
# Insert the elements into stack by calling push 

print(s.peek())
#Get the Top most element of stack using the peek

s.display()
#display function displays all elements present in the stack

d = s.pop()
#pops out the top most element present in stack

print("Popped out",d,"from stack")
s.display()
