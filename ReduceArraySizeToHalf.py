class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        maparr = {}
        count = 0
        k = len(arr)/2
        res = 0
        for x in arr:
            maparr[x] = maparr.get(x,0)+1
        ordered = sorted(maparr.items(), key=lambda x: x[1],reverse = True)
        
        for i in range(len(ordered)):
            count += ordered[i][1]
            res+=1
            if count >= k:
                break
        return res
