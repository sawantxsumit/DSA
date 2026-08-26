class solution():
    def twoSum(self , nums,target):
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]]= i

                   
        for i in range(len(nums)): 
            complement= target-nums[i]
            if complement in nums and hash_table[complement] !=i:
                return [i,hash_table[complement]]
            
            
                
                
l=solution()

num=[2,5,5,11]
target=10
res=l.twoSum(num,target)
        
print(res)

# res=l.twoSum(num,target)
# print(res)
                