class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        for r,n in enumerate(nums):
            k -= (1-n)
            if k < 0:
                k += 1-nums[l]
                l+=1
            count = max(count,r-l+1)
        return count
