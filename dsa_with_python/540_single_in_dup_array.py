'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 
'''

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1

        while low<high:

            mid=(low+high)//2

            if mid%2 ==1:
                mid=mid-1 #to make it even
            if nums[mid]!=nums[mid+1]:
                high=mid
            else:
                low=mid+2
        return nums[low]
    
l=Solution()
nums=[1,1,2,3,3,4,4,7,7,8,8]
a=l.singleNonDuplicate(nums)
print(a)
