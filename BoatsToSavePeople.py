class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        l,r = 0,len(people)-1
        while l<r:
            if people[l] + people[r] <= limit:
                count+=1
                l+=1
                r-=1
            else:
                count +=1
                r-=1
        if l==r:
            count+=1
        return count
