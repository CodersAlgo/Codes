import numpy as np

class circular_queue() :
    
    def __init__(self,size) :
        self.size = size+1
        self.queue = np.array([None]*(self.size))
        self.front = 0
        self.rear = 0
        
    def isempty(self) :
        if self.front == self.rear :
            return True
        else :
            return False
        
    def isfull(self) :
        if (self.rear+1)%self.size == self.front :
            return True
        else :
            return False
        
    def enqueue(self,element) :
        if self.isfull() :
            print("Queue is full cannot enqueue the element")
            return
        else :
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = element
            return "Given element inserted sucessfully"
        
    def dequeue(self) :
        if self.isempty() :
            return "Queue is empty cannot dequeue the element"
        else :
            self.front = (self.front+1)%self.size
            output = str(self.queue[self.front]) + " dequeued"
            return output
        
    def print_queue(self) :
        print("\nPrinting elements of queue :- ")
        temp = self.front
        while temp != self.rear :
            temp = (temp+1)%self.size
            print(self.queue[temp],end="\t")
        print("\n")

# creating a circular queue of size 5            
qu = circular_queue(5)

# inserting 5 elements into the circular queue
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(7)
qu.enqueue(0)
qu.enqueue(1)
qu.print_queue()

# Trying to insert 6 th element
qu.enqueue(5)

# dequeuing two elements for space 
print(qu.dequeue())
print(qu.dequeue())

# Inserting new elements in free space 
qu.enqueue(5)
qu.enqueue(6)

# printing values present in queue after insertion
qu.print_queue()