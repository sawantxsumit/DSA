'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
#method 1
def sortedSquares( nums):
        # if not nums:
        #     return []
        
        # sqr_nums=[num*num for num in nums]
        # sqr_nums.sort()
        # return sqr_nums
        return sorted(x*x for x in nums )

#mthod 2
#did'nt pass all test cases

# from collections import deque
# def sortedSquares(nums):
#         answer=deque()
#         l,r=0,len(nums)-1
#         while l<=r:
#             left, right= abs(nums[l]), abs(nums[r])
#             if left>right:
#                 answer.appendleft(left**2)
#                 l+=1
#                 print(answer)
#             else:
#                 answer.appendleft(right**2)
#                 r-=1
#                 print(answer)
#         return list(answer)
    
nums=[-4,-1,0,3,10 ,6]
res=sortedSquares(nums)
print(res)