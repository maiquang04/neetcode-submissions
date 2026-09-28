class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(p, (target - p) / s) for p, s in zip(position, speed)]
        arr.sort(key=lambda e: e[0], reverse=True)

        res = []

        for e in arr:
            if not res or e[1] > res[-1][1]:
                res.append(e)
        
        return len(res)
                



                