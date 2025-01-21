class Solution:
    def hammingWeight(self, n: int) -> int:
        #Bin return the binary rep with 0b prefix for telling the computer
        #that we are using binary representation
        return [int(bit) for bit in bin(n)[2:]].count(1)