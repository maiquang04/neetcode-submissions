class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lim = len(nums) // 3
        m = defaultdict(int)
        res = []

        for num in nums:
            m[num] += 1

            if len(m) <= 2:
                continue

            temp = defaultdict(int)
            for k, v in m.items():
                if v > 1:
                    temp[k] = v - 1
            
            m = temp

        for num in m.keys():
            if nums.count(num) > lim:
                res.append(num)

        return res
