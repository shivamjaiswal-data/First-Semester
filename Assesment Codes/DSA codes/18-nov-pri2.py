
class Node:
    def __init__(self,pid,name,pr):
        self.pid = pid
        self.data = name
        self.priority = pr
        self.next = None


class PriorityQueue:

    def __init__(self):
        self.front = self.rear = None

    # 1. Add Patient
    def enqueue(self,new_node):

        if self.front == None:  # first node
            self.front = self.rear = new_node
            return

        if self.front.priority > new_node.priority:  # insert at first
            new_node.next = self.front
            self.front = new_node
            return

        else:
            temp = self.front

            while temp:
                if new_node.priority < temp.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next

            prev.next = new_node
            new_node.next = temp

            if temp == None:
                self.rear = new_node

    # 2. Display next patient
    def display_next(self):

        if self.front == None:
            print("No patients waiting")
            return

        print("\nNext Patient:")
        print("Patient ID:",self.front.pid)
        print("Name:",self.front.data)
        print("Priority:",self.front.priority)

    # 3. Remove patient after treatment
    def dequeue(self):

        if self.front == None:
            print("No patients to treat")
            return

        temp = self.front

        print("Patient treated:",temp.data)

        self.front = self.front.next

        if self.front == None:
            self.rear = None

    # 4. Display all waiting patients
    def display_all(self):

        if self.front == None:
            print("No patients waiting")
            return

        temp = self.front

        print("\nAll Waiting Patients:")

        while temp:
            print("ID:",temp.pid,
                  "Name:",temp.data,
                  "Priority:",temp.priority)

            temp = temp.next


# Main program

pq = PriorityQueue()

while True:

    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient After Treatment")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        pr = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if pr >= 1 and pr <= 3:
            pq.enqueue(Node(pid,name,pr))
            print("Patient added successfully")
        else:
            print("Invalid priority. Enter 1, 2 or 3.")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Exiting Hospital Management System")
        break

    else:
        print("Invalid choice")
