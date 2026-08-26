'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
'''
def subArraysum(nums,k):
    n=len(nums)
    subArr=[]
    for i in range(n):
        for j in range(i , n):
            subArr.append(sum(nums[i:j+1]))
    return subArr.count(k)
nums=[1,1,1]
print(subArraysum(nums,2))