class Solution(object):
    def removeOuterParentheses(self, s):
        stack = []
        depth = 0

        for i in range(len(s)):
            if s[i] == "(":
                if depth > 0:
                    stack.append(s[i])
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    stack.append(s[i])

        return "".join(stack)