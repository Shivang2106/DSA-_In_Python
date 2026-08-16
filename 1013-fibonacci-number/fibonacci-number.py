class Solution(object):
    def fib(self, n):
        a, b = 0, 1
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        i = 1
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
        
        return c