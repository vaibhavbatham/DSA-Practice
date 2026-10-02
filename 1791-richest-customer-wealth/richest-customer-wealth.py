class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        max_wealth = float("-inf")

        for account in accounts :
            max_wealth = max(max_wealth , sum(account))

        return max_wealth