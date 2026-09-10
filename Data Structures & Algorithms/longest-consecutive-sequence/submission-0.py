class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        res = 0

        for num in nums:
            len = 0
            if num - 1 not in m:
                while num in m:
                    len += 1
                    num += 1
                res = max(res, len)

        return res