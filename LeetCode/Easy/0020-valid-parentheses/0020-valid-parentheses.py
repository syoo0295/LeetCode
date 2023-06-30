class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack 
        stack = []
        brackets_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # if char is an open bracket, push it on the the stack
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                # if stack is empty or top of the stack is not the corresponding opening bracket, return False.
                if not stack or stack[-1] != brackets_map[char]:
                    return False
                stack.pop()
        return len(stack) == 0