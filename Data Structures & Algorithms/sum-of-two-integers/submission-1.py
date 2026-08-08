class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask in hexadecimal
        mask = 0xFFFFFFFF
        
        # Max positive value for a 32-bit signed integer
        maximum = 0x7FFFFFFF
        
        while b != 0:
            # Calculate the carry
            carry = (a & b) << 1
            
            # Calculate the sum without the carry
            a = (a ^ b) & mask
            
            # Assign the carry to b for the next iteration
            b = carry & mask
            
        # If 'a' is negative, we need to handle Python's arbitrary precision
        if a <= maximum:
            return a
        else:
            return ~(a ^ mask)