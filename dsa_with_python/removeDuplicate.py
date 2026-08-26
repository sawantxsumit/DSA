def removeDup(nums):
    a=set(nums)
    nums=list(a)
    nums.sort()
    print(nums)
    return len(nums)

n=[1,1,2]
print(removeDup(n))