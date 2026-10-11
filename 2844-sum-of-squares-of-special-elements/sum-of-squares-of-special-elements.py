class Solution(object):
    def sumOfSquares(self, nums):
        result = 0
        n = len(nums)
        for i in range(n):
            if n%(i+1) == 0:
                result += nums[i]*nums[i]
        return result 