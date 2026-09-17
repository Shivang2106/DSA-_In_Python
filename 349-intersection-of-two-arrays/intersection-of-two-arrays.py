class Solution(object):
    def intersection(self, nums1, nums2):
        a=list(set(nums1))
        b=list(set(nums2))
        result=[ ]
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    result.append(a[i])
        return result