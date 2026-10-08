class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check  = set()
        left =0 
        max_length = float("-inf")
        if len(s) == 0:
            max_length = 0

        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left+=1

            check.add(s[right])
            length = right - left + 1
            max_length = max(max_length , length)
        
        return max_length