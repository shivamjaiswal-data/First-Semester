class node :
    def __init__(self,data,next = None):
        self.data = data 
        self.next = next

n1 = node(12)
n2 = node(13)
n3 = node(14)
n1.next  = n2 
n2.next  =  n3 


t1  =  n1 

print(t1.data)
print(t1.next.next.data)