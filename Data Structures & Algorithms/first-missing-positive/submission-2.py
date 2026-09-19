class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 0 < val <= len(nums):
                nums[val - 1] = -1 * abs(nums[val - 1]) 
            elif val == 0:
                nums[i] = len(nums) + 1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1