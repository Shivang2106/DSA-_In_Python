class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        for i in nums:
            a=i*i
            result.append(a)
        result.sort()
        return result