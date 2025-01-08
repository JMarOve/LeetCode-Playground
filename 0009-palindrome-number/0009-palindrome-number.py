class Solution:
    def isPalindrome(self, x: int) -> bool:
        var=list(filter(lambda i:(i),str(x)))
        return(var==var[::-1])