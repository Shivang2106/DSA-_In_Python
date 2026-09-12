class Solution(object):
    def findDuplicates(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                result.append(nums[i])
        return result