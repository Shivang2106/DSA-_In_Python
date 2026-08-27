class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]