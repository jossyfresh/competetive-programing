class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        x =sum(chalk)
        if k%x==0:
            return 0
        y = k%x
        for i in range(len(chalk)):
            y-=chalk[i]
            if y<0:
                return i
