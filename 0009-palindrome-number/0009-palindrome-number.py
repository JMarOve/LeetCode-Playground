#Just a fancy solution using Lambda functions. Is it needed? Nop, but it is just cool.
#class Solution:
   # def isPalindrome(self, x: int) -> bool:
    #    var=list(filter(lambda i:(i),str(x)))
     #   return(var==var[::-1])
#Same solution can be achieved with a classic var=list(str(x)) 

#Solution withouth converting it into a string. Really ugly. 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False
        original_number=x
        reverse_number = 0 
        while original_number>0:
            reverse_number=reverse_number*10+original_number%10
            original_number=original_number//10 
        return x==reverse_number