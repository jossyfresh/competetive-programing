class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        c = []
        last = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            z = math.sqrt(x**2 + y**2)
            c.append([z,x,y])
        c.sort()
        for i in range(0,k):
            last.append([c[i][1],c[i][2]])
        return last
