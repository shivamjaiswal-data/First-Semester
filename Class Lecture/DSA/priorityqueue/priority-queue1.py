
class node:
    def __init__(self, value, pr):
        self.value = value
        self.priority = pr
        self.next = None


class priorityQueue:

    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):

        if self.front == None:
            self.front = new_node
            self.rear = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next:
            if new_node.priority <= temp.next.priority:
                break

            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next == None:
            self.rear = new_node

    def display(self):
        temp = self.front

        while temp:
            print(temp.value, temp.priority, end=" | ")
            temp = temp.next

        print()


pq = priorityQueue()

pq.enqueue(node(100, 2))
pq.enqueue(node(200, 3))
pq.enqueue(node(300, 6))
pq.enqueue(node(400, 8))

pq.display()
