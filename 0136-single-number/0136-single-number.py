#XOR operation. XOR(A,A)=0. And XOR is additive. 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, v: total ^ v, nums)