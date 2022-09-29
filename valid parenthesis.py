class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        diction = {")":"(","]":"[","}":"{"}
        for i in s:
            if i in diction.values():
                stack.append(i)
            elif stack and stack[-1] == diction.get(i):
                stack.pop()
            else :
                return False
        return stack == []
