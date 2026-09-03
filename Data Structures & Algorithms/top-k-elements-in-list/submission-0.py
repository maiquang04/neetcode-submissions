class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        arr = list(m.items())
        arr.sort(reverse=True, key= lambda x: x[1])

        return [key for key, val in arr[:k]]