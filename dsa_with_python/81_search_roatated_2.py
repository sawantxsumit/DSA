'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low=0
        high=len(nums)-1
        
        while(low<=high):
            mid= (low+high)//2
            
            if target== nums[mid]:
                return True
            
            if nums[mid]==nums[low]==nums[high]: # edge case
                low=low+1
                high=high-1
                continue #incase this condition becomes true again
                        
            if nums[low]<=nums[mid]:
                if target<=nums[mid] and target>=nums[low]:
                    high= mid-1
                
                else:
                    low=mid+1
            else: 
                if target>=nums[mid] and target<=nums[high]:
                    low=mid+1
                                
                else:
                    high= mid-1
        
        return False
        
nums=[3,1,2,3,3,3,3]
target=3
l=Solution()
a=l.search(nums , target)
print(a)