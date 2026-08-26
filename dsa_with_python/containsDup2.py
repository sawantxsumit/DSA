'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()  # Store elements in a sliding window
        for i in range(len(nums)):
            if nums[i] in seen:
                return True  # Found a duplicate within k distance
            
            seen.add(nums[i])  # Add the current number to the set

            if len(seen) > k:  # Keep the window size within k
                seen.remove(nums[i - k])  # Remove the oldest element
            
        return False
    
l=Solution()
# num=[1,0,1,1]
# k=1
num=[1,2,3,1,2,3]
k=2
# num=[99,99]
# k=2
res=l.containsNearbyDuplicate(num,k)
print(res)