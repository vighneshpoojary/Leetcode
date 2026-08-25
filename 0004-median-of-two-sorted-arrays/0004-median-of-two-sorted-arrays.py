class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums1.extend(nums2)
        nums1 = sorted(nums1)

        k = len(nums1)

        if k % 2 == 0:
            low = nums1[k // 2 - 1]
            high = nums1[k // 2]
            return (low + high) / 2.0

        else:
            return float(nums1[k // 2])