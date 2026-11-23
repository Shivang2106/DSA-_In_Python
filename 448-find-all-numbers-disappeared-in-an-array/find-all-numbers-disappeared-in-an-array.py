class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        unlisted = list()
        
        nums.sort()
        nums = list(set(nums))
        read = 0
        
        for i in range (1, n + 1):
            if read > len(nums) - 1 or i != nums[read]:
                unlisted.append(i)
            else:
                read += 1       
        
        return unlisted