class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string=s.split(" ")
        print(string)
        word=""
        while string[-1]=="":
            string.pop(-1)
        return(len(string[-1]))