class Solution(object):
    def maxDepth(self, s):
        depth = 0
        max_depth = 0
        for ch in s:
            if ch == "(":
                depth+=1
                if depth > max_depth:
                    max_depth = depth
            if ch == ")":
                depth-=1
        return max_depth