'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''
#method 1
# def three_sum(nums):
#     nums.sort()
#     ans=[]
#     for i in range(len(nums) - 2):  # First pointer
#         if i > 0 and nums[i] == nums[i - 1]:  
#             continue  # Skip duplicate values
        
#         j, k = i + 1, len(nums) - 1  # Two-pointer approach
#         while j < k:
#             s = nums[i] + nums[j] + nums[k]
#             if s == 0:
#                 ans.append([nums[i], nums[j], nums[k]])
#                 j += 1
#                 k -= 1
                
#                 # Skip duplicates
#                 while j < k and nums[j] == nums[j - 1]:
#                     j += 1
#                 while j < k and nums[k] == nums[k + 1]:
#                     k -= 1
#             elif s < 0:
#                 j += 1
#             else:
#                 k -= 1
                
#     return ans

#method 2
def three_sum(nums):
    nums.sort()
    ans=[]
    
    for indx , val in enumerate(nums):
        #check for duplicate values
        if indx>0 and nums[indx]==nums[indx-1]:
            continue
        
        left=indx+1
        right= len(nums)-1
        
        while left<right:
            sum= val+nums[left]+ nums[right]
            if sum<0:
                left+=1
            elif sum>0:
                right-=1
            else:
                ans.append([val ,nums[left], nums[right]])
                left+=1
                
                while left<right and nums[left]==nums[left-1]:
                    left+=1
    return ans

nums=[-1,0,1,2,-1,-4]
print(three_sum(nums))
    
          