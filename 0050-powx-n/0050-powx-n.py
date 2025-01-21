class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        sign = -1 if n<0 else 1
        n = abs(n)
        res = 1
        while n>0:
            if n&1==0:
                x*=x
                n//=2
            else:
                res*=x
                n-=1
        return res if sign==1 else 1/res