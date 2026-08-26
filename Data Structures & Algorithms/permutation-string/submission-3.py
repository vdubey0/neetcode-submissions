from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
        
        for c in s2[:len(s1)]:
            s2_count[ord(c) - ord('a')] += 1

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            if s1_count == s2_count:
                return True
            
            s2_count[ord(s2[l]) - ord('a')] -= 1

            l += 1
            r += 1

            if r < len(s2):
                s2_count[ord(s2[r]) - ord('a')] += 1

        return False

            



            
