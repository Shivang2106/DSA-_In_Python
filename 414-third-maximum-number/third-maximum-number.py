class Solution(object):
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort()

        if len(nums) == 1:
            return nums[0]

        elif len(nums) == 2:
            return nums[1]

        else:
            return nums[-3]