class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_value = float("-inf")
        total = 0
        for i in nums:
            total += i
            max_value = max(max_value , total)
            if total < 0 :
                total = 0

        return max_value
