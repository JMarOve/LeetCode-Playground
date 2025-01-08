#Just a fancy solution using Lambda functions. Is it needed? Nop, but it is just cool.
#Same solution can be achieved with a classic var=list(str(x)) 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        var=list(filter(lambda i:(i),str(x)))
        return(var==var[::-1])