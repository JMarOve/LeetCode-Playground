#Romans were really practical, but let's do a hashmap, again XD

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1,
        }

        modified_string = s
        modified_string = modified_string.replace("IV","IIII")
        modified_string = modified_string.replace("IX","VIIII")
        
        modified_string = modified_string.replace("XL","XXXX")
        modified_string = modified_string.replace("XC","LXXXX")
        
        modified_string = modified_string.replace("CD","CCCC")
        modified_string = modified_string.replace("CM","DCCCC")

        return sum([hash_map[i] for i in list(modified_string)])