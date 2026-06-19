# def BubbleSort(nums):
#     if nums[0]>nums[1]:
#         nums[0], nums[1] = nums[1],nums[0]
#     return nums

# nums=[5,4,3,1,2]
# print(BubbleSort(nums))

# 2nd way
# def BubbleSort(nums):
#     L=len(nums)
#     for i in range(L):
#         if nums[0]>nums[1]:
#             nums[0], nums[1] = nums[1],nums[0]
#     return nums 
        
# nums=[5,4,3,1,2]
# print(BubbleSort(nums))

# 3rd way
def BubbleSort(nums):
    L=len(nums)
    c=0
    for j in range(L):
        swapped=False
        for i in range(L-1-j):
            c+=1
            if nums[i]>nums[i+1]:
                nums[i], nums[i+1] = nums[i+1],nums[i]
                swapped=True
            print(c,j,i,nums)
        if not swapped:
            break
    return nums 
        
nums=[2,4,1,9]
print(BubbleSort(nums))