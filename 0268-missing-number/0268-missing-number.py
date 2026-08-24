class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        k = len(nums)
        count = 0
        for i in range(k):
            if nums[0]!=0:
                return 0
            if k == 1 and  nums[0]!=0:
                return 0
            if k == 1 and nums[0]==0:
                return nums[i]+1
            if i == k-1:
                return nums[i]+1
            if nums[i]+1  == nums[i+1]:
                continue
            else:
                return nums[i]+1
            


        