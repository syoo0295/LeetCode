class Solution:
    def isPalindrome(self, x: int) -> bool:
        # base case: if x is negative or if the last digit is 0, it returns false
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x //= 10
        
        
        return x == reverse_num or x == reverse_num // 10