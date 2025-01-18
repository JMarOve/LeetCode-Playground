class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        aux=0
        for i in range(len(digits)):
            aux+=(10**(len(digits)-i-1))*digits[i]
        aux+=1
        return [int(d) for d in list(str(aux))]
        