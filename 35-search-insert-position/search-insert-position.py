class Solution(object):
    def searchInsert(self, nums, target):
        nums.sort()
        for i in range(len(nums)):
            if target==nums[i]:
                return i
                break
            elif nums[i]<target:
                continue
            else:
                if nums[i]>target:
                    return i
                    break
        if target>nums[i]:
            return i+1
        