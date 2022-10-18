class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num:
            while stack and int(x) < int(stack[-1]) and k!=0:
                k-=1
                stack.pop()
            stack.append(x)
        stack = stack[:len(stack)-k]
        ans = "".join(stack)
        return str(int(ans)) if ans else "0"
