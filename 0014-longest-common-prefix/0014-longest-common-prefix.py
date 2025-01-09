#We can order alphabetically the strings, so we only need to compare the first word with the last one. 
#And we only need to iterate through the characters of the first word
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedlist = sorted(strs)
        result = ""
        for element in range(len(sortedlist[0])):
            if sortedlist[0][element] == sortedlist[len(sortedlist)-1][element]:
                result+= sortedlist[0][element]
            else:
                return result
        return result
        