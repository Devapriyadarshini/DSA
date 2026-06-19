nums=input().split()
l=len(nums)
c=0
for i in range(l):
    for j in range(i+1,l):
        c+=1
        print(c,i,j,nums[l-i-1])
