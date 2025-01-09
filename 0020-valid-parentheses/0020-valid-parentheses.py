##Classic problem with Stacks structure

class Solution:
    def isValid(self, s: str) -> bool:
    
        hash_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for char in s:
            if char in hash_map:  # If it's a closing bracket
                # Pop the last element in the stack or use a placeholder if empty
                top_element = stack.pop() if stack else '#'
                # Check if the top element matches the corresponding opening bracket
                if hash_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # Stack should be empty if all brackets are matched
        return not stack