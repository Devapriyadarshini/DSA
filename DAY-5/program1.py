# sum of all numbers
# nums=input()
# t=int(input())
# c=0
# for i in nums:
#     if i.isdigit() and int(i)==t:
#         c+=1
# print(c)


# nums=input().split()
# print(nums)

#sum of square of all numbers
#printing square of all numbers
# nums=input().split()
# s=1
# for i in nums:
#      x=int(i)*int(i)
#      print("square",x)
# print("sum",s)

#print all unique pair combinations
nums=input().split(",")
l=len(nums)
for j in range(l):
    for i in range(j+1,l):
        print(nums[j],nums[i])

    
