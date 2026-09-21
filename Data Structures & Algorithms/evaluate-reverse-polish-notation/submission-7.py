class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                a = s.pop()
                b = s.pop()
                if t == '+':
                    s.append(a + b)
                elif t == '-':
                    s.append(b - a)
                elif t == '*':
                    s.append(a * b)
                elif t == '/':
                    s.append(int(b / a))
            else:
                s.append(int(t))

        return s.pop()