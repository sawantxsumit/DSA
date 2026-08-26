'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
'''
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res=[]
        for i in range(len(nums)):
            count=0
            for num in nums:
                if nums[i]>num:
                    count+=1
            res.append(count)
        return res
                
                
        
l=Solution()

num=[6,6,6,6]

res=l.smallerNumbersThanCurrent(num)
        
print(res)        