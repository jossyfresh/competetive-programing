class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i,x in enumerate(nums):
            if x%2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        prefixSum = {0:1}
        Sum = 0
        res = 0
        for n in nums:
            Sum += n 
            x = Sum - k
            res+=prefixSum.get(x,0)
            prefixSum[Sum]= 1 + prefixSum.get(Sum,0)
        return res
