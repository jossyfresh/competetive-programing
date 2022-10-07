class Solution:
    def maxScore(self, arr: List[int], K: int) -> int:
        N, i, j = len(arr), 0, len(arr) - K
        Max = total = sum(arr[j:])
        for _ in range(K):
            total += arr[i] - arr[j]
            Max = max(Max, total)
            i += 1
            j += 1
        return Max
