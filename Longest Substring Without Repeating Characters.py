class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        if len(s) == 1:
            return 1
        for r in range(1,len(s)):
            while s[r] in s[l:r]:
                res = max(res,(r-l))
                l+=1
            res = max(res,(r-l)+1)
            r+=1
        return res
