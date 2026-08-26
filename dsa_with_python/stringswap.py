'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
'''
#method 1 -> by me
def check_equal(s1,s2):
    if s1==s2:
        return True
    elif s1[1:len(s1)-1]==s2[1:len(s2)-1]:    
        if s1[0]==s2[len(s2)-1] and s1[len(s1)-1] == s2[0]:
            return True
    else:
        return False
    
s1="siyolsdcjthwsiplccjbuceoxmpjgrauocx"
s2="siyolsdcjthwsiplccpbuceoxmjjgrauocx"
print(check_equal(s1,s2))

#method 2 ->gpt
# def can_be_equal_with_one_swap(s1: str, s2: str) -> bool:
#     if s1 == s2:
#         return True
    
#     # Collect the indices where the characters are different
#     diff = [(a, b) for a, b in zip(s1, s2) if a != b]

#     # Check if there's exactly 2 differences and they are swappable
#     return len(diff) == 2 and diff[0] == diff[1][::-1]

# print(can_be_equal_with_one_swap("siyolsdcjthwsiplccjbuceoxmpjgrauocx", "siyolsdcjthwsiplccpbuceoxmpjgrauocx"))