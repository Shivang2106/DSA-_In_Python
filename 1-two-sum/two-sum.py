class Solution:

    def twoSum(self, nums, target):

        mp = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in mp:
                return [mp[complement], i]

            mp[nums[i]] = i


# Creating object
obj = Solution()

nums = [2, 7, 11, 15]
target = 9

result = obj.twoSum(nums, target)

print(result)