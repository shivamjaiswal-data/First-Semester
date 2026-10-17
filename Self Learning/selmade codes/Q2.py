class node:
    def __init__(self,val):
        self.data = val
        self.next = None
class Linkedlist :
    def __init__(self):
        self.head = None
    
    def append(self,new_node):
            if self.head == None :
    
                self.head = new_node
            else:
                temp = self.head 
    
                
                while temp.next :
                    temp = temp.next 
                temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next 
my_list = Linkedlist()
my_list.append(node(10))
my_list.append(node(20))
my_list.append(node(30))
my_list.append(node(40))
my_list.display()
