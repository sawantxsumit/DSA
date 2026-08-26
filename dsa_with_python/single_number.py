'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,1]
Output: 1
'''
from collections import Counter
def singleNumber(nums):
    # a=Counter(nums)
    # least_common=a.most_common()[-1][0]
    # return least_common

    # xor = 0
    # for num in nums:
    #     xor ^= num
    
    # return xor
    for num in nums:
        if nums.count(num)==1:
            return num
        

            
num=[4,1,2,1,2]
a=singleNumber(num)
print(a)