'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
'''



class solution():
    def twoSum(self , nums,target):
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        hash_table = {}
                   
        for i in range(len(nums)): 
            complement= target-nums[i]
            if complement in nums:
                return [i,hash_table[complement]]
            hash_table[nums[i]]= i
            
            
                
                
l=solution()

num=[2,5,5,11]
target=10
res=l.twoSum(num,target)
        
print(res)

# res=l.twoSum(num,target)
# print(res)
                