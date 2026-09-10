class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in s:
            if num - 1 not in s:
                length = 0
                cur = num

                while cur in s:
                    length += 1
                    cur += 1
                
                res = max(length, res)

        return res