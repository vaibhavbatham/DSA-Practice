class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}

        for ch in s:
            dict1[ch]  = dict1.get(ch , 0 ) + 1
        
        for ch in range(len(s)) :
            if dict1[s[ch]] == 1 :
                return ch
            
        return -1
