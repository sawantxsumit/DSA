'''
Question : Find first and last position of elements in sorted array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
'''
class A():
    def first_and_last(self , nums , target):
        
        # Find first occurence
        
        low=0
        high=len(nums)-1
        first=-1
                
        while low<=high:
            mid=(low+high)//2
            
            if target> nums[mid]:
                low=mid+1
                
            elif target< nums[mid]:
                high=mid-1
                
            else:
                first=mid
                high=mid -1 # search left
                
        #find second occurence
        low=0
        high=len(nums)-1
        last=-1
        
        while low<=high:
            mid= (low+high)//2
            
            if target> nums[mid]:
                low=mid+1
                
            elif target<nums[mid]:
                high=mid-1
                
            else:
                last=mid
                low=mid+1  #search right
                
        return [first, last]
    
    
l=A()
nums=[5,7,7,8,8,10]
target=8
a=l.first_and_last(nums , target)
print(a)
    
    
        
                