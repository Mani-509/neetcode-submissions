class Solution:
    def guessNumber(self, n: int) -> int:
        if n==1:
            return n
        high,low=n,0
        while low<=high:
            mid=(low+high)//2
            if guess(mid)==0:
                return mid  
            elif guess(mid)==-1:
                high=mid-1
            else:
                low=mid+1
        

    
            

        