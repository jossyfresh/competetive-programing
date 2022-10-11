class Solution:
    def carPooling(self, trips: List[List[int]], k: int) -> bool:
        passanger = [0]*1001
        for x in trips:
            numpass,fromi,toi = x
            passanger[fromi]+= numpass
            passanger[toi]-=numpass
        capacity = 0
        for i in range(1000):
            capacity +=passanger[i]
            if capacity > k:
                return False 
        return True
