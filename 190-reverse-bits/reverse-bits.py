class Solution(object):
    def reverseBits(self, n):
        a = bin(n)[2:].zfill(32)
        b = a[::-1]
        return int(b,2)