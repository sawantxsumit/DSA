def check(nums):
    count=0
    n=len(nums)
    for i in range(len(nums)):
        if nums[i]>nums[(i+1)%n]:
            count+=1
        if count>1:
            return False
    
    return True
            

nums=[3,4,5,1,2]
# nums=[1,2,3,4]
print(check(nums))
        