'''
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 
Example 1:
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
'''

# method 1 -> time limit exceeded (Brute force)
# def reverse_pairs(nums):
#     count=0
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]> nums[j]*2:
#                 count+=1
#     return count

#method 2
def reverse_pairs(nums):
    def merge_sort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2

            count = 0

            # left half
            count += merge_sort(left, mid)

            # right half
            count += merge_sort(mid + 1, right)

            j = mid + 1

            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1

                count += j - (mid + 1)

            #merge
            temp = []
            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1

            for k in range(len(temp)):
                nums[left + k] = temp[k]

            return count

    return merge_sort(0, len(nums) - 1)
    


nums=[1,3,2,3,1]
num2=[]
for n in nums:
    num2.append(n*2)
    
print(num2)
print(reverse_pairs(nums))