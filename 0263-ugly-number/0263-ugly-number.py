class Solution:
    def isUgly(self, n: int) -> bool:
        ugly_primes = [2,3,5]
        if n<=0:
            return False
        else:
            for prime in ugly_primes:
                while n%prime == 0:
                    n=n//prime
        return n == 1