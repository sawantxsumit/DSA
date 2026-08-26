'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

use a set which contains only unnique values to solve this 
'''


class Solution(object):
    def containsDuplicate(self, nums):
        
        #here a is a set and we will check whether elements of the list are present in a or not 
        #if a doesnt contain that element we'll simply add the element into the set
        
        a=set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        return False
                 
l=Solution()
num=[1,2,3,4,5,3]
res=l.containsDuplicate(num)
print(res)

                
                
                