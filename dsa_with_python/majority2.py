'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]
'''
# def majority(nums):
#     n=len(nums)
#     res=[]
#     print(n//3)
#     if n==1:
#         return nums
#     for num in nums:
#         if nums.count(num)> n//3:
#             res.append(num)
#     res=set(res)
    
#     return list(res)
def majority(nums):
    hashmap={}
    for num in nums:
        if num not in hashmap:
            hashmap[num]=1
        else:
            hashmap[num]+=1
    res=[]
    for key  in hashmap:
        if hashmap[key] > len(nums)//3:
            res.append(key)
    return res

nums=[3,2]
print(majority(nums))