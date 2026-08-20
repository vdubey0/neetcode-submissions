class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        end = 0
        max_len = 0
        mp = {}


        while end < len(s):
            if s[end] in mp:
                front = max(mp[s[end]] + 1, front)
            
            mp[s[end]] = end
            max_len = max(max_len, end - front + 1)
            end += 1
        
        return max_len