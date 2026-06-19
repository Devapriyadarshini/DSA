# nums=[2,4,6,9,5,3,7,8]
# def split(nums):
#     L=len(nums)
#     return [nums[0:L//2],nums[L//2:]]
# print(split(nums))


def merge_lists(L1,L2):
    i,j=0,0
    res=[]
    while i<len(L1) or j<len(L2):
        if L1[i]<L2[J]:
            res.append(L1[i])
            i+=1
        else:
            res.append(L2[i])
            j+=1
    res.extend(L1[i:])
    res.extend(L2[j:])
            

