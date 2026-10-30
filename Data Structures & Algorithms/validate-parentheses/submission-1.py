class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif bracket == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif bracket == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif bracket == '}':
                if not stack or stack.pop() != '{':
                    return False
        
        return len(stack) == 0