"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(self, s: str, t: str) -> bool:
    sc = [0]*26
    tc = [0]*26
    for c in s:
        sc[ord(c)-ord('a')]+=1
    for c in t:
        tc[ord(c)-ord('a')]+=1
    for i in range(26):
        if tc[i]!=sc[i]:
            return False
    return True
