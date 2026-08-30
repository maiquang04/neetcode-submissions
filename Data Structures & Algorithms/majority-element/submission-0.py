class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)
        cnt = [0, 0]

        for num in nums:
            m[num] += 1

            if m[num] > cnt[0]:
                cnt[0] = m[num]
                cnt[1] = num

        return cnt[1]