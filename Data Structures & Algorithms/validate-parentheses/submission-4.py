class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenMap = {
            "}" : "{", 
            "]" : "[",
            ")": "(",
        }
        stack = []

        for b in s:
            if b in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)

        return True if not stack else False