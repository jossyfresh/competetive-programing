class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        y = []
        for i in s:
            if i == ")":
                while stack:
                    x = stack.pop()
                    if x != "(":
                        y.append(x)
                    else:
                        break
            else:
                stack.append(i)
            for j in y:
                stack.append(j)  
                y = []  
        return ''.join(stack)
