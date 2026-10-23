class node :
    def  __init__ (self,val):
        self.data =  val 
        self.next = None 
class LinkedList:
    def __init__(self):
        
        self.head = None
    def append(self,val):
        temp = node(val)
        if(self.head != None):
            t1 = self.head
            while(t1.next!= None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' -> ')
            temp = temp.next 
        print("NuLL")
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

my_list.display()

