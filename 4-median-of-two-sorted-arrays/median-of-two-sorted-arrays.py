
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        i = j = 0
        nums3 = []

        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while i < n1:
            nums3.append(nums1[i])
            i += 1

        while j < n2:
            nums3.append(nums2[j])
            j += 1

        total = n1 + n2

        if total % 2 == 1:
            return nums3[total // 2]
        else:
            val = total // 2
            return (nums3[val] + nums3[val - 1]) / 2.0
