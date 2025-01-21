'''Very mediocre solution 
       s=list(str(num))
        print(s)
        res = 0
        while len(s)!=1:
            for integer in s:
                res+=int(integer)
            s = list(str(res))
            res = 0
        return int(s[0])
        '''
class Solution:

    def addDigits(self, num: int) -> int:
   
        return 0 if num==0 else (1 +(num-1)%9)