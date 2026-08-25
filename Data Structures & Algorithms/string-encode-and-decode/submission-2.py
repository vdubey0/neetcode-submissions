class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}#{s}' 

        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        strs = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            one_str = s[j+1 : j+1+length]
            strs.append(one_str)
            i = j + 1 + length
        
        return strs
                

            