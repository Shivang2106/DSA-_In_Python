class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        mid = len(nums) // 2
        target = nums[mid]
        step = 0

        for i in range(len(nums)):
            step += abs(nums[i] - target)

        return step