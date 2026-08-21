from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        close_to_open = dict(zip(close_brackets, open_brackets))

        q = deque()

        for c in s:
            if c in open_brackets:
                q.append(c)
            
            if c in close_brackets:
                if not q or close_to_open[c] != q.pop():
                    return False
                
        if q:
            return False
        
        return True

        