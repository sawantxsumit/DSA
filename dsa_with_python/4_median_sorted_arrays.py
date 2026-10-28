'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m=len(nums1)
        n=len(nums2)
        low=0
        high=m
            
        while low<=high:
            m1=(low+high)//2
            m2=(m+n+1)//2 - m1
            
            if m1==0:
                l1=float('-inf')
            else:
                l1=nums1[m1-1]
            
            if m1==m:
                r1=float('inf')
            else:
                r1=nums1[m1]
                
            if m2==0:
                l2=float('-inf')
            else:
                l2=nums2[m2-1]
                
            if m2==n:
                r2=float('inf')
            else:
                r2=nums2[m2]
                
            if l1<=r2 and l2<=r1:
                if (m+n)%2==1:
                    return max(l1,l2)
                
                return (max(l1,l2)+min(r1,r2))/2.0
            
            elif l1>r2:
                high=m1-1
            else:
                low=m1+1
                
                
a=Solution()
nums1 = [1,3]
nums2 = [2]
print(a.findMedianSortedArrays(nums1, nums2))
            
