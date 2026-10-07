class Solution(object):
    def intersect(self, nums1, nums2):
        list1 = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                list1.append(nums1[i])
                nums2.remove(nums1[i])

        return list1