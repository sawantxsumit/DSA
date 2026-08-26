'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
'''
def max_consecutive(nums):
    # r=len(nums)-1
    # pcount, count=0,0
    # while r>=0:
    #     pcount=count
    #     count=0
    #     while nums[r] !=0 and r>=0:
    #         count+=1
    #         r-=1
    #     r-=1
    #     count=max(count, pcount)
    # return count
    
    #method 2
    max_count=count=0
    for num in nums:
        if num==1:
            count+=1
            max_count=max(count, max_count)
        else:
            count=0
    return count

n=[1,1,0,1,1,1]
print(max_consecutive(n))