import math

class Solution:
    def climbStairs(self, n: int) -> int:
        # Binet's Formula constants for finding the n-th Fibonacci number:
        # F(n) = (phi^n - psi^n) / sqrt(5)
        sqrt5 = math.sqrt(5)
        
        # phi (Φ) is the Golden Ratio (~1.618033...)
        phi = (1 + sqrt5) / 2
        
        # psi (ψ) is the conjugate of the Golden Ratio (~ -0.618033...)
        psi = (1 - sqrt5) / 2
        
        # The number of ways to climb 'n' stairs corresponds to the (n + 1)-th Fibonacci number.
        # e.g., for n = 1 stair, ways = 1 (which is F_2)
        #       for n = 2 stairs, ways = 2 (which is F_3)
        # Therefore, we shift the index by 1 to align with Binet's formula indices.
        n += 1
        
        # Apply Binet's Formula and round to the nearest integer to eliminate 
        # any minor floating-point precision inaccuracies.
        return round((phi**n - psi**n) / sqrt5)