'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
'''
#method 1
# from collections import Counter
# def majority(nums):
#     return Counter(nums).most_common()[0][0]

#method 2
def majority(nums):
    l=len(nums)
    for n in nums:
        if nums.count(n)> l/2:
            return n
    

nums = [3,2,3]
print(majority(nums))