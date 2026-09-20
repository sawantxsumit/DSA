'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at 
an unknown index k (1 <= k < nums.length) such that the resulting array 
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 
'''
class A():
    def rotated_array(self  , nums , target):
        low=0
        high=len(nums)-1
        
        while(low<=high):
            mid= (low+high)//2
            
            if target== nums[mid]:
                return mid
            
            # if left array is sorted
            if nums[low]<=nums[mid]:
                if target<=nums[mid] and target>=nums[low]:
                    high= mid-1
                
                else:
                    low=mid+1
            # if right array is sorted
            else: 
                if target>=nums[mid] and target<=nums[high]:
                    low=mid+1
                                
                else:
                    high= mid-1

        return -1
    
    
# nums = [4,5,6,7,0,1,2]
nums=[5,1,3]
target = 5
l=A()
s=l.rotated_array(nums , target)
print(s)