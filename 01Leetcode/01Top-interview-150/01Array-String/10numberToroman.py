class Solution(object):
    def intToRoman(self, num):
        number_dict = {
                       1000:"M", 900:"CM", 
                       500:"D", 400:"CD", 
                       100:"C", 90:"XC", 
                       50:"L", 40:"XL", 
                       10:"X", 9:"IX", 
                       5:"V", 4:"IV", 
                       1:"I" 
                    }
        
        rom = ""
        # print(number_dict.items(), 'line 14') # full dictionary
        for number_key, roman_value in number_dict.items():
            while  num >= number_key:
                rom += roman_value
                num -= number_key
        return rom
                              
input_num = int(input('Enter a integer number: '))
# print(input_str)
sl = Solution()
res = sl.intToRoman(input_num)
print('Number', input_num, 'convert to roman: ', res)