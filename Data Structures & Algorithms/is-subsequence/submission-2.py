class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        s_ix = 0
        
        for i in range(len(t)):
            if t[i] == s[s_ix]:
                s_ix += 1
                
            if s_ix == len(s):
                return True

        return False