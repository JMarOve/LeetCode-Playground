class Solution:
    def reverse(self, x: int) -> int:
        ubound = 2**31-1
        lbound = -2**31
        sign = -1 if x< 0 else 1
        x = abs(x)
        x = list(str(x))[::-1]
        res=0
        for i in range(len(x)):
            res += 10**(len(x)-i-1)*int(x[i])
            
        res *= sign
        if res < lbound or res>ubound:
            return 0
        else:
            return res