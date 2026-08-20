class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front = 0
        end = 0
        substr = set()
        max_len = 0

        while end < len(s):
            while s[end] in substr:
                substr.remove(s[front])
                front += 1  
               
            substr.add(s[end])
            end += 1

            max_len = max(max_len, len(substr))
        
        return max_len