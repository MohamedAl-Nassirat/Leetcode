class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            total.append(sums)
        return total