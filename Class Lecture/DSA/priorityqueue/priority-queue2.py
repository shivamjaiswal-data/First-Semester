class Node:
    def __init__(self,value,pr):
        self.data = value
        self.priority = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self,new_node):
        if self.front == None: #first node to  be inserted
            self.front = new_node
            return
        if self.front.priority>new_node.priority: #insert at first position
            new_node.next = self.front #link new node next to front
            self.front = new_node #add new node
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


    def display(self):
        temp = self.front
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
        print()

#create priority queue
pq = PriorityQueue()
pq.enqueue(Node(100,2))
pq.enqueue(Node(500,6))
pq.enqueue(Node(300,3))
pq.enqueue(Node(600,1))
pq.display()