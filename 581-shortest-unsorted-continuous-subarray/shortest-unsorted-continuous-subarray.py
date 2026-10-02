class Solution(object):
    def findUnsortedSubarray(self, nums):
        start = -1
        end = -1
        max_num = nums[0]
        min_num = nums[-1]
        for i in range(len(nums)):
            if nums[i] < max_num:
                end = i
            else:
                max_num = nums[i]
            j = len(nums) - 1 - i
            if nums[j] > min_num:
                start = j
            else:
                min_num = nums[j]
        return 0 if start == -1 else end - start + 1