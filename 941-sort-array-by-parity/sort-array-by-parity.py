class Solution(object):
    def sortArrayByParity(self, nums):
        l1=[]
        l2=[]
        for i in range(len(nums)):
            if nums[i]%2!=0:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        l2.extend(l1)
        return l2