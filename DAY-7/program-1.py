# minimum
nums=list(map(int,input().split()))
curr_min=nums[0]
for i in range(len(nums)):
    if curr_min>nums[i]:
        curr_min=nums[i]
print(curr_min)