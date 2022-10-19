class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       stack = []
       operation = "+*-/"
       result = 0
       for i in tokens:
           if  i in operation:
               y = int(stack.pop())
               x = int(stack.pop())
               if i == "+":
                   result = x+y
               elif i == "-":
                   result = x-y
               elif i == "*":
                   result = x*y
               else:
                   result = int(x/y)
               stack.append(result)
           else:
               stack.append(i)
       return stack[0]
