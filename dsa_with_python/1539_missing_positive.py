'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
'''

#brute force
# class Solution(object):
#     def findKthPositive(self, arr, k):
#         """
#         :type arr: List[int]
#         :type k: int
#         :rtype: int
#         """
#         n=1
#         count=0
#         for i in range(0,(len(arr)+k)):
#             if n not in arr:
#                 count+=1
#                 if count==k:
#                     return n
                
#             n+=1

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k

            
a=Solution()
arr = [1,2,3,4]
k = 2
print(a.findKthPositive(arr,k))