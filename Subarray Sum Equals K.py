class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {0:1}
        Sum = 0
        res = 0
        for n in nums:
            Sum += n
            x = Sum-k
            res+=prefixsum.get(x,0)
            prefixsum[Sum] = 1 + prefixsum.get(Sum,0)

        return res
