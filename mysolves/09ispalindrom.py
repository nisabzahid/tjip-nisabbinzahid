class Solution:
    def isPalindrome(self, x: int) -> bool:
        half = 0
        if x <0 or (x!=0 and x%10 ==0):
            return False
        while half < x:
            half *= 10 
            half += x %10
            x //=10
        
        return x==half or x==half//10