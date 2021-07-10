import numpy as np 

class queue() :
    
    def __init__(self,size) :
        self.size = size
        self.q = np.array([None]*self.size)
        self.front = self.rear = -1
        
    def isempty(self) :
        if self.front == self.rear :
            return True
        else :
            return False
        
    def isfull(self) :
        if self.rear == self.size-1 :
            return True
        else :
            return False 
        
    def enqueue(self,data) :
        if not self.isfull() :
            self.rear += 1
            self.q[self.rear] = data
        else :
            print("\nQueue is full cannot insert ",data,"\n")
            
    def dequeue(self) :
        if not self.isempty() :
            self.front += 1
            return self.q[self.front]
        else :
            print("\nQueue is empty cannot dequeue\n")
            
    def get_values(self) :
        if not self.isempty() :
            print("\nValues present in queue are :- ",end = " ")
            for x in range(self.front+1,self.rear+1) :
                print(self.q[x],end="\t")
            print()
        else :
            print("\nQueue is empty there are no values to print \n")
        
qu = queue(5)

qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(5)
qu.get_values()
qu.dequeue()
qu.get_values()