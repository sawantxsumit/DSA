'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        #method 1 -> slow
        # print(nums)
        # for i in range(len(nums)+1):  
        #     if i not in nums:
        #         return i
        #method 2 ->faster
        # for i,v in enumerate(nums):
        #     if i!=v:
        #         return i
        #     if v==len(nums)-1:
        #         return v+1
        #method 3 -> 0ms runtime
        return sum(range(len(nums)+1)) - sum(nums)
            
            
            
l=Solution()

num=[3,0,1,5,4,6,7,9,2]
res=l.missingNumber(num)
print(res)
            
        