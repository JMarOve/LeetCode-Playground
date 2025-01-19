class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f"{n:032b}"
        #Format to have the binary representation
        #Going back
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
        