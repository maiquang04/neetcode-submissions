class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            while True:
                if not s:
                    s.append(a)
                    break
                elif s[-1] * a > 0 or s[-1] < 0 and a > 0:
                    s.append(a)
                    break
                elif abs(s[-1]) > abs(a):
                    break
                elif abs(s[-1]) == abs(a):
                    s.pop()
                    break
                else:
                    s.pop()
                
        return s

