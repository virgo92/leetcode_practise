class Solution:
    def isValid(self, s: str) -> bool:

        imap = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            if char in imap:
                top_ele = stack.pop() if stack else '#'
                if top_ele != imap[char]:
                    return False
            else:
                stack.append(char)

        return not stack