class Solution(object):
    def smallestIndex(self, nums):
        total = 0
        i=0
        while len(nums)>i:
            total = sum(int(d) for d in str(nums[i]))
            if total == i:
                return i
            i+=1
        return -1