class Solution:
    def pivotIndex(self, a: List[int]) -> int:
        b = a.copy()
        for i in range(1,len(a)):
            a[i]+=a[i-1]  
        for j in range(2,len(a)+1):
            b[-j]+=b[-j+1]
        res = -1
        for i in range(len(a)):
            if a[i]==b[i]:
                res = i 
                break

        return res
