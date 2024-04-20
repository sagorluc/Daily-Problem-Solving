class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse_numter = 0
        temp = x
        
        while temp != 0:
            last_digit = temp % 10 # last digit
            reverse_numter = reverse_numter * 10 + last_digit # store digit in reverse number
            temp //= 10 # rest of x number
            
        if reverse_numter != x:
            return False
        return True
            

input_x = int(input('Enter a number.. '))
sl = Solution()
ans = sl.isPalindrome(input_x)
print(ans)