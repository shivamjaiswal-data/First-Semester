# HW print sum of 2 consecutive nodes in SLL
class Node:                                   
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self, head = None):
        self.head = head
        
    def append(self, data):
        temp = Node(data)
        
        if(self.head == None):
            self.head = temp
            temp.next = self.head
            return
            
        t1 = self.head

        while(t1.next != self.head):
            t1 = t1.next
        t1.next = temp
        temp.next = self.head
        
    def insert(self, data, pos):
        temp = Node(data)
        if pos == 1:
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            temp.next = self.head
            self.head = temp
            t1.next = self.head
            return
        p = 1
        t = self.head
        while p != pos - 1 and t.next != None:
            t = t.next
            p += 1

        temp.next = t.next
        t.next = temp
            
            
    
    def insertAtBeg(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    
    def delete(self, data):
        
        # If list is empty
        if self.head is None:
            return

        # If head node has to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        # Search for the node
        temp = self.head

        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                return

            temp = temp.next
            if(temp.next == None):
                print("Not present")
                return
    def reverse(self):
        curr = self.head
        prev = None
        while(curr):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        self.head = prev
        
    def sum_of_node(self):
        temp = self.head
        sum = 0
        while(temp.next != None):
            a = temp.next.data
            sum = temp.data + a
            temp = temp.next
            
        
        print(sum)
    
    def search_middle_data_del(self):
        #check if SLL is empty
        if(self.head is None):
            print("Linckedln list is empty")
            return
        i = self.head     # its moves only one node 
        j = self.head      #its moves two nodes
        prev = None
        while(j != None and j.next != None):
            prev = i
            i  = i.next
            j = j.next.next
        
        print('Find the data :- ' , i.data) #prints middle value
        prev.next = i.next
        i = None
        
    def delete_first_last(self):
        self.head = self.head.next
        temp = self.head.next
        prev = None
        while(temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        temp = None
        
    def del_alternate(self):
        prev = self.head
        temp = self.head.next
        while(prev and temp):
            prev.next = temp.next
            temp = None      #delete a node
            prev = prev.next
            temp = prev.next
            if(prev):
                temp = prev.next
                
    def concatenate(self):
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = obj1.head
        
    def prints(self):
        t1 = self.head
        
        while(True):
            print(t1.data , end = " -> ")
            t1 = t1.next
            if(t1 == self.head):
                break
        print(t1.data)
        
    
obj = SLL()
obj1 = SLL()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
obj.append(5)
obj.insert(0 , 6)
obj.prints()
'''


obj1.append(1)
obj1.append(2)
obj1.append(3)
obj1.append(4)
obj1.append(5)
print("First List :- ")
obj.print()
print('Second List :- ')
obj1.print()
print("Concatination :- " , '\n')
obj.concatenate()
obj.print()
'''