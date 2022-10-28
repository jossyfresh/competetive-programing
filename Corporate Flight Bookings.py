class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        PrefixSum = []
        for (s,e,pas) in bookings:
            PrefixSum.append((s-1,pas))
            PrefixSum.append((e,-pas))
        res = [0]*n
        for x in PrefixSum:
            if x[0] < n:
                res[x[0]] += x[1]
            else:
                continue
        for i in range(1,len(res)):
            res[i]+=res[i-1]
        return res
