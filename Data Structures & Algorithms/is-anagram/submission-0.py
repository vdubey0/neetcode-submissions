class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = {}
        for c in s:
            if c not in s_counts:
                s_counts[c] = 1
            else:
                s_counts[c] += 1

        t_counts = {}
        for c in t:
            if c not in t_counts:
                t_counts[c] = 1
            else:
                t_counts[c] += 1

        for c in s_counts:
            if c not in t_counts:
                return False

            if t_counts[c] != s_counts[c]:
                return False
            
        return True