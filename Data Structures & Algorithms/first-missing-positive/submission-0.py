class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1

        while True:
            if res in nums:
                res += 1
            else:
                break

        return res