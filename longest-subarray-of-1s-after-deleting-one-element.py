class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        countzero = 0
        res = 0
        while r < len(nums):
            if nums[r]:
                r+=1
                res = max(res,r-l)
            elif nums[r] == 0 and countzero == 1:
                countzero -= 1 - nums[l] 
                l+=1
            else:
                r+=1
                countzero+=1
                res = max(res,r-l)
        return res-1
