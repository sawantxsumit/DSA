'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
#method 1
# def sortColors(nums):
#     c=[]
#     for i in range(3):
#         c.append(nums.count(i))
#     print(c)
#     a=0
#     j=0
#     for n in c:
#         for i in range(n):
#             nums[j]=a
#             j+=1
#         a+=1

#method 2
# DNF -> Dutch national flag algorithm
def sortColors(nums):
    n=len(nums)
    mid=low=0
    high=n-1
    while mid<=high:
        if nums[mid]==0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid+=1
            low+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high], nums[mid]= nums[mid], nums[high]
            high-=1

#method 3
# def sortColors(nums):
#     num=nums[:]
#     j=a=0
#     for c in range(0,3):
#         for i in range(num.count(a)):
#             nums[j]=a
#             print(a)
#             j+=1
#         a+=1
nums = [2,0,2,1,1,0]   
sortColors(nums)
print(nums) 
    