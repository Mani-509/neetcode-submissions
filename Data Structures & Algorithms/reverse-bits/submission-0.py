class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Extract the rightmost bit of n
            bit = (n >> i) & 1
            # Shift the extracted bit to its new reversed position and add it to res
            res = res | (bit << (31 - i))
        return res
        
        