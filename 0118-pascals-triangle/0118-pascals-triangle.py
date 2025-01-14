def fact(n)->int:
    return int(n*fact(n-1)) if n!=0 else 1
def comb(n:int,k:int)->int:
    return int(fact(n)/(fact(k)*fact(n-k)))
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            new_row=[comb(i,k) for k in range(i+1) ]
            res.append(new_row)
        return res


