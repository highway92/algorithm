class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hash = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char not in hash:
                stack.append(char)
            elif not stack or hash[char] != stack.pop():
                return False

        return len(stack) == 0