class node :
    def  __init__ (self,val):
        self.data =  val 
        self.next = None 
class LinkedList:
    def __init__(self):
        
        self.head = None
    def insert(self,val):
        temp = node(val)
        if(self.head != None):
            t1 = self.head
            while(t1.next!= None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
    
    def delete_negative(self):
        temp = self.head
        t1 = None

        while temp:
            if temp.data < 0:
                if temp == self.head:
                    self.head = temp.next
                    temp = self.head
                else:
                    t1.next = temp.next
                    temp = temp.next
            else:
                t1 = temp
                temp = temp.next
    def display(self):
            temp = self.head
            while temp:
                print(temp.data, end = ' -> ')
                temp = temp.next 
            print("NuLL")

my_list = LinkedList()
my_list.insert(10)
my_list.insert(20)
my_list.insert(30)
my_list.insert(-40)
my_list.insert(-50)
my_list.insert(60)
my_list.insert(-70)

my_list.delete_negative()

my_list.display()
   