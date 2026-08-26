'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

#method 1
# def moveZero(nums):
#     k=0
#     for i in range(len(nums)):
#         if(nums[i]!=0):
#             nums[k]=nums[i]
#             k+=1
#     for i in range(k, len(nums)):
#         nums[i]=0
#     print(nums)

#method 2
def moveZero(nums):
    left=0
    right=len(nums)
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left], nums[right] =  nums[right], nums[left]
            left+=1
    print(nums)

n=[0,1,0,3,12]
(moveZero(n))