class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        maximum = max(nums)
        points = [0] * (maximum + 1)
        for num in nums:
            points[num] += num
        prev2 = 0
        prev1 = 0
        for i in range(maximum + 1):
            current = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = current
        return prev1