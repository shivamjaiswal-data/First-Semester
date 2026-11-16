class node :
    def __init__(self,value,pr):
     self.value = value
     self.priority = pr
     self.next = None
class priorityQueue:
   def __init__(self):
      self.front = self.rear = None
   def enqueue(self,new_node):
      if self.front.priority > new_node.priority:
         new_node.next = self.front
         self.front = new_node
         return
      else:
         temp = self.front
         while temp.next :
            if new_node.priority <= temp.priority:
               break
            else:
               temp = temp.next
               