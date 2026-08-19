from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_map = {}

        for word in strs:
            chars = frozenset(Counter(word).items())

            if chars not in chars_map:
                chars_map[chars] = [word]
            else:
                chars_map[chars].append(word)
        
        return list(chars_map.values())

