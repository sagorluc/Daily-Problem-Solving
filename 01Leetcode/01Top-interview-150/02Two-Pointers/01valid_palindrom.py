import re
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        if s == "":
            return True
        
        if s[::-1] in s: # backward check with forward
            return True
        else:
            return False
        
                
input_str = input('Enter an array: ').lower()
# print(input_str)
alpha_char = ''.join(char for char in input_str if char.isalpha()) # alphabet character only
# print(alpha_char)
sl = Solution()
res = sl.isPalindrome(alpha_char)
print("Is Palindrom: ", res)