class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if x == '(' and c != ')':
                    return False
                if x == '{' and c != '}':
                    return False
                if x == '[' and c != ']':
                    return False
        
        if len(stack) == 0:
            return True
        return False
                


                   
        