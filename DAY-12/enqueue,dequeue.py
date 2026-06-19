# Enqueue implementation
Front = 0
Rear = -1
queue =[None]*5
size = 0
def enqueue(value):
    if size == len(queue):return False
    rear +=1
    size +=1
    quueue[rear]=value
    return True
def dequeue():
    if size==0:return False
    front +=1
    return True
def peek():
    return queue[Front]
def isFull ():
    return size==len(queue)
def isempty():
    return size==0