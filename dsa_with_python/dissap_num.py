class Solution(object):
    def findDisappearedNumbers(self, nums):
       
        #method 1-> failed in test case with huge amount of data (time limit exceeded)
        # a=[]
        # set_nums=set(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in set_nums:
        #         a.append(i)
        # return a
        
        #method 2
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # Get index based on value
            nums[index] = -abs(nums[index])  # Mark as visited (negative)
    
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
            
             
l=Solution()

num=[4,3,2,7,8,2,3,1]
# num=[1,1]
# set_num=set(num)
# print(set_num)

res=l.findDisappearedNumbers(num)
print(res)