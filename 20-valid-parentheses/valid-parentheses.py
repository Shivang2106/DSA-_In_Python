class Solution(object):
    def isValid(self, s):
        stack =[]
        mapping = {")":"(","}":"{","]":"["}
        for chr in s:
            if chr in mapping.values():
                stack.append(chr)
            elif chr in mapping.keys():
                if not stack or mapping[chr] != stack.pop():
                    return False
        return not stack