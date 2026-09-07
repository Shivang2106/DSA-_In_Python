class Solution(object):
    def runningSum(self, nums):
        result =[]
        s=0
        for i in range(len(nums)):
           s=s+nums[i]
           result.append(s)
        return result 