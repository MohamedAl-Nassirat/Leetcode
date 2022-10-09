class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
            [100,4,200,1,3,2]
        """
              
        # O(n) runtime
        numSet = set(nums)
        longest_consec = 0
        for i in numSet:            
            if (i-1) not in numSet:
                length = 0
                while(length + i) in numSet:
                    length += 1
                longest_consec = max(length, longest_consec)
        return longest_consec
                       
                
            