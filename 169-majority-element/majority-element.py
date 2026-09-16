class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        result= len(nums)/2
        return nums[result]