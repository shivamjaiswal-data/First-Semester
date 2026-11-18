class ListNode:
    def __init__ (self,val=0,next=None):
        self.val= val
        self.next = next 
class Solution:
    def createlist(self,values):
        head =None
        temp = None
        for val in values:
            new_node = ListNode(val)
            if head == None:
                head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = temp.next
        return head
    def display(self, head):
        temp = head 
        while(temp):
            print(temp.val,end=" -> ")
            temp = temp.next
        print("None")
    def insert (self,head,value,pos):
        new_node = ListNode(value)
        if pos == 0:
            new_node.next = head
            return new_node
        temp= head
        for i in range(pos-1):
            if temp == None:
                return head 
            temp = temp.next
        if temp == None:
            return head
        new_node.next = temp.next
        temp.next = new_node
        return head 
    def middle (self, head):
        slow= head
        fast =  head 
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next 
        return slow
    def deletNode(self,head,value):
        if head == None:
            return head
        if head.val == value:
            return head.next
        temp = head 
        while(temp.next):
            if temp.next.val == value:
                temp.next = temp.next.next

        return head
    def reverseList(self,head):
        prev = None
        temp= head
        while(temp):
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        return prev
    def consecutiveSum(self,head):
        temp = head 
        result = []
        while (temp and temp.next):
            total =  temp.val + temp.next.val
            result.append(total)
            temp = temp.next
        return result 
s = Solution()
head =  s.createlist([10,20,30,40,40,50])
s.display(head)
# head= s.insert(head,25,2)
# s.display(head)
mid = s.middle(head)
print("Middle:",mid.val if mid else None)