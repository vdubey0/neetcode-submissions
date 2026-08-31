class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            i = 0
            while i < min(len(prefix), len(s)) and prefix[i] == s[i]:
                i += 1
            
            prefix = prefix[:i]

        return prefix
                