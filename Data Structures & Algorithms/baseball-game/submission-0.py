class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for op in operations:
            if op == '+':
                a = s[-1]
                b = s[-2]
                s.append(a + b)
            elif op == 'D':
                a = s[-1]
                s.append(a * 2)
            elif op == 'C':
                s.pop()
            else:
                s.append(int(op))
        
        return sum(s)