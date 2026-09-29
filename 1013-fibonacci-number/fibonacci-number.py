class Solution:
    def rec (self , n):
    
        if n == 0 or n == 1: 
            return n

        return self.rec(n-1) + self.rec (n - 2)
        
    def fib(self, n: int) -> int:
        
        return self.rec(n)
 