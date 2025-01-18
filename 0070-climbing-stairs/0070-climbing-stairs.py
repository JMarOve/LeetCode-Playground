'''def fibonaccimod(x):
    res = 0
    if x<=2:
        return x
    else:
        return fibonaccimod(x-1)+fibonaccimod(x-2)
'''
#This works but excedded time limit

class Solution:
    def climbStairs(self, n: int) -> int:
        array = [1,1]

        for i in range(2,n+1):
            array.append(array[-1]+array[-2])
        return array[-1]