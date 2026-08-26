'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
'''

class Solution(object):
    def longestMountain(self, arr):
        mountain=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] >arr[i+1]:
                l=i-1
                r=i+1
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                mountain= max(mountain , r-l+1) #to find the max length of the mountain
        return mountain
    
a=Solution()
arr=[2,2,2]
print(a.longestMountain(arr))

                