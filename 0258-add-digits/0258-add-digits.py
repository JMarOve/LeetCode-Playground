class Solution:
    def addDigits(self, num: int) -> int:
        s=list(str(num))
        print(s)
        res = 0
        while len(s)!=1:
            for integer in s:
                res+=int(integer)
            s = list(str(res))
            res = 0
        return int(s[0])