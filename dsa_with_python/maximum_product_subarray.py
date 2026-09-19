'''
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class solution():
    def maxProduct(self , nums):
        max_so_far=nums[0]
        min_so_far=nums[0]
        answer=nums[0]
        
        for i in range(1,len(nums)):
            current=nums[i]
            
            old_max=max_so_far
            old_min=min_so_far
            
            # Calculate and update the maximum and minumium
            # We have three varibale to test for max and min which are
            variables= [current , old_max*current , old_min*current]
            
            max_so_far=max(variables)
            min_so_far=min(variables)
            answer= max(max_so_far , answer)
            
        
        return answer
            
l=solution()
# nums=[2,3,-2,4]
nums=[-2,3,-4]
a=l.maxProduct(nums)
print(a)
            