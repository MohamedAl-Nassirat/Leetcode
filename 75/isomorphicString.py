class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # E : A
        # G : D
        # G : D --> Valid

        # F : B
        # O : A
        # O : R --> Invalid, O maps to A and R

        mapA, mapB = {}, {}

        for i in range(len(s)):
            
            if ((s[i] in mapA and mapA[s[i]] != t[i]) or (t[i] in mapB and mapB[t[i]] != s[i])):
                return False
            
            mapA[s[i]] = t[i]
            mapB[t[i]] = s[i]
        return True

            