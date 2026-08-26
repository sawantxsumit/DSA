'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
'''
#Counter is a class from Python’s built-in collections module. It's like a dictionary specifically designed for counting how many times each element appears in a collection (like a string, list, or tuple).
#method 2 -> gpt
# from collections import Counter
# def valid_anagram(s,t):
#     return Counter(s)==Counter(t)

#method 1 by me
def valid_anagram(s,t):
    l=[]
    if len(s) !=len(t):
        return False
    else:
        for char in t:
            l.append(char)
        for char in s:
            if char in l:
                l.remove(char)
            else:
                return False
        if l==[]:
            return True
        return False

#method 3
# def valid_anagram(s,t):
#     return sorted(s)==sorted(t)

#method 4
# def valid_anagram(s, t):
#     if len(s) != len(t):
#         return False

#     count = [0] * 26  # For 'a' to 'z'
#     count1 = [0] * 26  

#     for i in range(len(s)):
#         count[ord(s[i]) - ord('a')] += 1
#         count[ord(t[i]) - ord('a')] -= 1

#     return count==count1

# s = "anagram"
# t = "nagaram"
s='rat'
t='car'
print(valid_anagram(s,t))