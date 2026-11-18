# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
        
#     def isEmpty(self):
#         return self.top is None
    
#     def push(self, new_node):
#         new_node.next = self.top
#         self.top = new_node
        
#     def pop(self):
#         if self.isEmpty():
#             print('Stack is Empty')
#         else:
#             temp = self.top
#             poped_data = temp.data
#             self.top = self.top.next
#             temp = None
#             return poped_data
            
#     def print(self):
#         if self.isEmpty():
#             print('Stack is Empty')
#         else:
#             print('Stack Contains...')
#             temp = self.top
#             while temp:
#                 print(temp.data)
#                 temp = temp.next



# class LQueue:
#     def __init__(self):
#         self.front = self.rear = None
#     def isEmpty(self):
#         return self.front is None
    
#     def enqueue(self, data):
#         if self.rear:
#             self.rear.next = data
#             self.rear = data
#         else:
#             self.front = self.rear=data 
#     def dequeue(self):
#         temp = self.front
#         dque = temp.data
#         self.front = self.front.next
#         if(self.front == None):
#             print('Queue is Empty Now')
#             self.rear = None
#         temp = None
#         return dque
        
#     def print(self):
#         if(self.front == None):
#             print('Queue is Empty Now')
#         else:
#             temp = self.front
#             while(temp):
#                 print(temp.data , end=' -> ')
#                 temp = temp.next
#             print('NULL')
    
# def reversed_stack(s1):
#     q1 = LQueue()
#     while not s1.isEmpty():
#         q1.enqueue(Node(s1.pop()))
#     #q1.print()
#     while not q1.isEmpty():
#         s1.push(Node(q1.dequeue()))
#     s1.print()
    
        
# s1 = Stack()
# s1.push(Node(10))
# s1.push(Node(100))
# s1.push(Node(45))
# s1.push(Node(40))
# reversed_stack(s1)



class node :
    def __init__ (self,val):
        self.data  = val
        self.next = None
class Lqueue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next =  new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self ):
        temp = self.front
        
        temp = self.front
        while temp:
            print(temp.data,end = "->")
            temp = temp.next
        print()
    def reverse_stack (s1):
        q1 =Lqueue()
        while not s1.isempty():
            q1.enqueue(node(s1.pop()))
        q1.print()
        while not q1.isempty():
            s1.push(node(q1.dequeue()))
        s1.print()

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp =  self.top 
            popped_data = temp.data
            self.top = self.top.next
            temp = None

class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            temp = self.top
            print("Popped Element:", temp.data)
            self.top = self.top.next
            temp = None

    def printstack(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack contains:")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next



que =Lqueue()
que.enqueue(node(10))
que.enqueue(node(20))
que.enqueue(node(30))
que.enqueue(node(40))
que.enqueue(node(50))

que.print()


st  = stack ()
st.push(node(10))
st.push(node(100))
st.push(node(14))
st.push(node(15))
st.push(node(27))
