class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        pair = [[pos,sp] for pos,sp in zip(position,speed)]
        
        for pos,sp in sorted(pair)[::-1]:
            time = (target - pos)/sp
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)        
