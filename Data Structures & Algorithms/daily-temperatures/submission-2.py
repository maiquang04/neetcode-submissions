class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        s = []

        for i in range(len(temps)):
            while True:
                if not s:
                    s.append(i)
                    break
                elif temps[i] > temps[s[-1]]:
                    res[s[-1]] = i - s[-1]
                    s.pop()
                else:
                    s.append(i)
                    break

        return res

