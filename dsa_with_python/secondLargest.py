def second_largest(nums):
    
    #method 1
    # if len(nums)<2:
    #     return nums
    # a=set(nums) #to remove the duplicate elements 
    # nums=list(a) # to assign back a into nums as a list because we cant access set using index
    # nums.sort() # sort the list
    # return nums[len(nums)-2]
    
    #method 2
    # a=max(nums)  #to find max in nums
    # nums.remove(a) #remove max from nums
    # a=max(nums) #again find max in nums which is second max
    # return a
    
    #method 3
    largest=0
    for n in nums:
        if n>largest:
            slargest=largest
            largest=n
        elif n<largest and n>slargest:
            slargest=n
    return slargest




nums=[11,2,33,55,34,3,4,5,7,7,8,78]
print(second_largest(nums))