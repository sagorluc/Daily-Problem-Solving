class Solution(object):
    def romanToInt(self, s):
        roman_dict = { 'I' : 1,
                       'V' : 5,
                       'X' : 10,
                       'L' : 50,
                       'C' : 100,
                       'D' : 500,
                       'M' : 1000 }
        
        res = 0
        
        for i in range(len(s)):
            current_value = roman_dict[s[i]]          
            if i < len(s)-1 and current_value < roman_dict[s[i+1]]:
               res = res - current_value
            else:
                res = res + current_value
                
        return res
                
                       
input_str = input('Enter a roman number: ').upper()
# print(input_str)
sl = Solution()
res = sl.romanToInt(input_str)
print('Roman', input_str, 'convert to numeric: ', res)