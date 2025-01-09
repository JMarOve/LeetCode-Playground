#Just the good old Newton's method
#We want to find the zeros of the function f(y)=y^2 - x
#df/dy=2y
#Newton method is xn+1=xn-f(x_n)/df(xn)
#Therefore xn+1 = xn- (xn^2-x)/2xn=1/2(xn+x/xn)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Return x directly for 0 and 1
        
        # Initial guess
        x0 = x / 2.0
        while True:
            x1 = 0.5 * (x0 + x / x0)  # Update using Newton's method
            if abs(x1 - x0) < 1:  
                break
            x0 = x1
        
        return int(x1)  