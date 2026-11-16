class node :
    def __init__(self,value,pr):
     self.value = value
     self.priority = pr
     self.next = None
class priorityQueue:
   
   def __init__(self):
      self.front = self.rear = None
   def enqueue(self,new_node):
      if self.front == None:
         self.front = new_node # first node to be inserted 
         return
      if self.front.priority > new_node.priority: # first position 
         new_node.next = self.front
         self.front = new_node
         return
      
      else:
        temp = self.front #traverse
        while temp:
            if new_node.priority<=temp.priority: #if priority is less keep moving forward
                break
            else:
                prev = temp
                temp = temp.next
        prev.next = new_node #insert betw low prio and high prio
        new_node.next = temp
      
      
   def diplay(self) :
      temp = self.front
      while temp :
         print(temp.value, end=" ")
         temp = temp.next
      print()
pq= priorityQueue()
pq.enqueue(node(100,2))
pq.enqueue(node(100,3))
pq.enqueue(node(100,6))
pq.enqueue(node(100,8))
pq.diplay()