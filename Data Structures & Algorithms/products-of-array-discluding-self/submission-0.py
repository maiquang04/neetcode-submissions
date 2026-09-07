class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = [1] * n
        y = [1] * n

        for i in range(1, n):
            x[i] = x[i - 1] * nums[i - 1]
            y[n - 1 - i] = y[n - i] * nums[n - i]
        
        return [i * j for i, j in zip(x, y)]