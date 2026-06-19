class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=None
    def insertAtstart(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.size+=1
            return
        newNode.next=self.head
        self.head=newNode
        self.size+=1
        return head
# How to insert with tail       
    def insertAtend(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.size+=1
            return
        self.tail.next=newNode
        self.tail=newNode
        return head
# How to insert without tail
    def insertAtend(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
            self.size+=1
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        self.size+=1
        curr.next=newNode
        return head
    def deleteAtstart(self):
        if self.head is None:
            return -1
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return self.head
    def deleteAtend(self):
        if self.head is None:
            return -1
        if self.head.next is None:
            self.head=None
            return
        curr=self.head
        while curr.next.next:
            curr=curr.next
        d=curr.next=None
        self.size-=1
        curr.next=None
        return d
    def display(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
    def deleteAtindex(self,index):
        if self.head is None:
            return -1
        if index==0:
            deleteAtstart()
            return


