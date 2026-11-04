class Solution(object):
    def minMoves(self, nums):
        nums.sort()
        step = 0
        for i in range(len(nums)):
            if nums[i] < nums[-1]:
                a = nums[-1]-nums[i]
                step += a
        return step