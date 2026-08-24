from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        max_char = None
        max_len = -1

        for r in range(len(s)):
            counts[s[r]] += 1

            if max_char is not None:
                if counts[s[r]] > counts[max_char]:
                    max_char = s[r]
            else:
                    max_char = s[r]

            substr_len = r - l + 1

            if substr_len - counts[max_char] <= k:
                max_len = max(max_len, substr_len)
            else:
                counts[s[l]] -= 1
                l += 1
                
        
        return max_len
            

            

