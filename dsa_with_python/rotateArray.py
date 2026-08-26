'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
'''

def rotate( nums, k):
    n=len(nums)
    k=k%n
    rotated=[0]*n
    for i in range(n):
       rotated[(i+k)%n]=nums[i]
    for i in range(n):
        nums[i]=rotated[i]
    return nums
    
   
    

n=[1,2,3,4,5,6,7]
print(rotate(n,3))
        