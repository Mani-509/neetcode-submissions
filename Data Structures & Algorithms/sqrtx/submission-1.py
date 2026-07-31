class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        guess = x / 2.0
    
    # Continuously update the guess using Newton's formula
        while True:
            better_guess = 0.5 * (guess + x / guess)
            
            # Check if the change is smaller than our allowed tolerance
            if abs(guess - better_guess) < 0.000000001:
                return int(better_guess)
                
            guess = better_guess
