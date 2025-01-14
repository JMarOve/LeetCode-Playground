#Specifying the maths behind Pascal's triangle

def fact(n)->int:
    return int(n*fact(n-1)) if n!=0 else 1
def comb(n:int,k:int)->int:
    return int(fact(n)/(fact(k)*fact(n-k)))
    
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        return [comb(rowIndex,k) for k in range(rowIndex+1) ]
