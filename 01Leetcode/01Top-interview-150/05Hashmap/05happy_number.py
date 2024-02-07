class Solution:
    def sum_of_number(self, num):
        ans = 0
        while num:
            digit = num % 10   # last digit of number
            digit = digit ** 2
            ans = ans + digit 
            num = num // 10    # next digit of number      
        return ans
    
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sum_of_number(n)            
            if n == 1:
                return True            
        return False
    
        
input_num = int(input("Enter a number: "))
sl = Solution()
res = sl.isHappy(input_num)
print("Is the number happy:", res)