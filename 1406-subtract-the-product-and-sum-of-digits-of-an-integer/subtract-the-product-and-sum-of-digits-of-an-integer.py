class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum1 = 0

        while n > 0:
            rem = n % 10       # Get last digit
            sum1 += rem        # Add digit to sum
            product *= rem     # Multiply digit
            n //= 10           # Remove last digit

        return product - sum1