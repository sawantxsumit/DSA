'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

The total number of subarrays in an array of size N is N * (N + 1) / 2.
'''
def largest_subarray(nums):
    
    max_sum=nums[0]
    curSum=0
    l=[]
    for num in nums:
        curSum+=num
        l.append(num)
        max_sum=max(max_sum, curSum)
        if curSum<0:
            curSum=0
            l=[]
    print(l)
        
    return max_sum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(largest_subarray(nums))