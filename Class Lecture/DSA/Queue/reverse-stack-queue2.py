class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top is None
    
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            temp = self.top
            poped_data = temp.data
            self.top = self.top.next
            temp = None
            return poped_data
            
    def print(self):
        if self.isEmpty():
            print('Stack is Empty')
        else:
            print('Stack Contains...')
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next



class LQueue:
    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, data):
        if self.rear:
            self.rear.next = data
            self.rear = data
        else:
            self.front = self.rear=data 
    def dequeue(self):
        temp = self.front
        dque = temp.data
        self.front = self.front.next
        if(self.front == None):
            print('Queue is Empty Now')
            self.rear = None
        temp = None
        return dque
        
    def print(self):
        if(self.front == None):
            print('Queue is Empty Now')
        else:
            temp = self.front
            while(temp):
                print(temp.data , end=' -> ')
                temp = temp.next
            print('NULL')
    
def reversed_stack(s1):
    q1 = LQueue()
    while not s1.isEmpty():
        q1.enqueue(Node(s1.pop()))
    #q1.print()
    while not q1.isEmpty():
        s1.push(Node(q1.dequeue()))
    s1.print()
    
        
s1 = Stack()
s1.push(Node(10))
s1.push(Node(100))
s1.push(Node(45))
s1.push(Node(40))
reversed_stack(s1)