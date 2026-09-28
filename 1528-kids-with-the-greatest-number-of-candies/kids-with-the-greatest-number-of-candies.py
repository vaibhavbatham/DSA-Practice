class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        max_value = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_value:
                ans.append(True)
            else:
                ans.append(False)

        return ans



