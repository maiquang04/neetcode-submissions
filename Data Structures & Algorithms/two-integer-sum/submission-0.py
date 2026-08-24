class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, num in enumerate(nums):
            val = target - num
            if val in s.keys():
                return [s[val], i]
            s[num] = i

        return []