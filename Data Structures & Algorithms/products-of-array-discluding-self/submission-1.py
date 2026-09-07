class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        temp = 1
        for i in range(1, n):
            res[i] = nums[i - 1] * temp
            temp = res[i]

        temp = 1
        for i in range(1, n):
            temp *= nums[n - i] 
            res[n - 1 - i] *= temp

        return res
