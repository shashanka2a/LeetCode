"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
"""



def validParanthesis(self, s: str) -> bool:
    d = {'(':')','[':']','{':'}'}
    stack = []
    for char in s:
        if char in d:
            stack.append(char)
        elif len(stack)==0 or d[stack.pop()]!=char:
            return False
    return len(stack)==0
