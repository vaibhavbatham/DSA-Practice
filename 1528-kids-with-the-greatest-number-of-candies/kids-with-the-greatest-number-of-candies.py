class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        ans = [(i + extraCandies) >= max(candies) for i in candies]
        return ans