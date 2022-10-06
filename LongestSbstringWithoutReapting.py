class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        char = set()
        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[l])
                l+=1
            char.add(s[i])
            res = max(res,len(char))
        return res
