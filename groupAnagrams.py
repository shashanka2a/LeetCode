"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

# O(NKlogK)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    d = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    return list(d.values())

# O(NK) 
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()
