'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
'''
#method 1
# def rearrange(nums):
#     p=[]
#     n=[]
#     for num in nums:
#         if num>0 or num==0:
#             p.append(num)
#         else:
#             n.append(num)
#     k=0
#     for i in range(0,len(nums),2):
#         nums[i]=p[k]
#         nums[i+1]=n[k]
#         k+=1
#     return nums

#method 2
def rearrange(nums):
    res=[0]* len(nums)
    p_index=0
    n_index=1
    for num in nums:
        if num>0:
            res[p_index]=num
            p_index+=2
        else:
            res[n_index]=num
            n_index+=2
    return res
nums = [3,1,-2,-5,2,-4]
print(rearrange(nums))         
    