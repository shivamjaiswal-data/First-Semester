class node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None
class linked_list :
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp =self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else: #First Node
            self.head = new_node
    def insert(self,new_node,pos):
        temp = self.head
        if pos == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            p =  1 
            while(p!= pos - 1 and temp.next) :
                temp = temp.next
                p+=1
            new_node.next = temp.next
           
            if temp.next:    # Last Node
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev =temp
    def reverse(self):
        temp = self.head
        if temp == None:
            print("List is empty")
            return 
        while temp.next:
            temp = temp.next 
        print("\nList elements in reverse order: ")
        while temp:
            print(temp.data, end = " ")
            temp = temp.prev
    
list = linked_list()
list.append(node(12))
list.append(node(16))
# list.print()
list.insert(node(5),1)
list.insert(node(53),2)

# list.print()
list.reverse()
