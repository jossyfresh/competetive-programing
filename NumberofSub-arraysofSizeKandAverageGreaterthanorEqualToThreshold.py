class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, T: int) -> int:
        l,r = 0,k
        j = len(arr)- k
        count = 0
        Sum = sum(arr[:k])
        while r < len(arr):
            if Sum/k >= T:
                count+=1
            Sum = Sum - arr[l] + arr[r]
            l+=1
            r+=1
        if Sum/k>=T:
            count+=1
        return count
