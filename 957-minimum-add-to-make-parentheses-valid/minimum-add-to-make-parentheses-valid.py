class Solution(object):
    def minAddToMakeValid(self, s):
        depth = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                if depth > 0:
                    depth -= 1
                else:
                    ans += 1

        return ans + depth