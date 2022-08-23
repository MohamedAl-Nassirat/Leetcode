class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = set(nums)
        if len(i) == len(nums):
            return False
        else:
            return True