class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        
        A,B = {}, {}
        
        for i in range(len(s)):
            A[s[i]] = 1 + A.get(s[i],0)
            B[t[i]] = 1 + B.get(t[i],0)
            
        return A == B