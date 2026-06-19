from collections import deque

q=deque()
q.append(10) # enque operation
q.append(20)
q.append(30)
print(q.popleft()) # deque operation
print(q[0]) # peek operation