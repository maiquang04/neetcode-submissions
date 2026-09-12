class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lim = len(nums) // 3
        m = defaultdict(int)
        res = []

        for num in nums:
            m[num] += 1

        for k, v in m.items():
            if v > lim:
                res.append(k)

        return res
