class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = 0
        right = len(nums) - 2
        nums[mid], nums[-1] = nums[-1], nums[mid]
        pivot = nums[-1]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums[left], nums[-1] = nums[-1], nums[left]

        return self.sortArray(nums[:left]) + [nums[left]] + self.sortArray(nums[left+1:])