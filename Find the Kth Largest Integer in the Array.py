class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        k =len(nums)-k
        x = str(nums[k])
        return x
