class Solution(object):
    def targetIndices(self, nums, target):
        li = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                li.append(i)
        
        return li