'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
def longest_sequence(nums):
    nums_set=set(nums)
    longest=0
    for num in nums_set:
        if num-1 not in nums_set:
            cur_num=num
            cur_streak=1
            
            while cur_num+1 in nums_set:
                cur_num+=1
                cur_streak+=1
            longest=max(cur_streak , longest)
    return longest
nums = [100,4,200,1,3,2]
print(longest_sequence(nums))
