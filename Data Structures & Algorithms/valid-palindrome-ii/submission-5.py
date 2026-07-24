class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, w = 0, len(s) - 1
        
        while low < w:
            if s[low] != s[w]:
                
                skip_low = s[low + 1 : w + 1]
                skip_w = s[low : w]
                
                return skip_low == skip_low[::-1] or skip_w == skip_w[::-1]
            
            low += 1
            w -= 1
            
        return True