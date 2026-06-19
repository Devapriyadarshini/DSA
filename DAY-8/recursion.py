# for i in range(10,0,-1):
#     print(i)

# i=20
# while i>10:
#     print(30-i)
#     i+=1
#     if i==30:
#         break
    
# i=20
# while i>10:
#     print(i-10)
#     i-=1    

# Recursion
# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)
# count(10)

# def Hello():
#     for i in range(5):
#         print(i)
#         if i==2:
#             return
#     print("Hello")
# print("Hello")

# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)
# count(10)

# Sum of first N Natural Numbers
def sum_n(n):
    if n <=0:
        return 0
    return n + sum_n(n-1)