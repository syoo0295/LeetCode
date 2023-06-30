class Solution:
    def isValid(self, s: str) -> bool:
       cto_o={')':'(',']':'[', '}':'{'}
       stack=[]
       for i in s:
           if i in cto_o:
              if stack and stack[-1] == cto_o[i]:
                   stack.pop()
              else:
                  return False
           else :
                stack.append(i)
       return False if stack else True