class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        for c in s:
            if c in ['(', '{', '[']:
                arr.append(c)
            elif len(arr) > 0 and (c == ')' and arr[-1] == '('
                or c == '}' and arr[-1] == '{'
                or c == ']' and arr[-1] == '['):
                arr.pop()
            else:
                return False
        
        return len(arr) == 0