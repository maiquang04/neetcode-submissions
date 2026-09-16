class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        m[0] = 1
        cur = 0
        res = 0

        for num in nums:
            cur += num

            res += m[cur - k]

            m[cur] += 1

        return res

