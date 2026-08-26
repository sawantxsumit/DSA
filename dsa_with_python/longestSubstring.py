'''
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer
'''
def longest_sub(s):
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the valid palindrome substring
    
    longest = ""
    
    for i in range(len(s)):
        # Odd-length palindrome (single character center)
        odd_pal = expand_around_center(i, i)
        # Even-length palindrome (double character center)
        even_pal = expand_around_center(i, i + 1)
        
        # Update longest palindrome found
        if len(odd_pal) > len(longest):
            longest = odd_pal
        if len(even_pal) > len(longest):
            longest = even_pal
    
    return longest


str='ababd'
res=[]
res=longest_sub(str)
print(res)