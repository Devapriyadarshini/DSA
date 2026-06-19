# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# Node1 = Node(10)
# Node2 = Node(20)
# Node1.data=30
# Node1.next=Node2
# Node1.next=None 
# print(Node1.data)

# Link 4 nodes
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# Node1 = Node(10)
# Node2 = Node(20)
# Node3 = Node(30)
# Node4 = Node(40)
# Node3.data=50
# Node1.next=Node2
# Node3.next=Node4
# Node4.next=None
# print(Node4.data)
l1=[4,5,3,7,6]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def createList(l1):
    head=None
    temp=head
    for i in l1:
        newNode=Node(i)
        if head is None:
            head=newNode
            temp=head
        else:
            temp.next=newNode
            temp=newNode
        
    return head
createList(l1)
    





