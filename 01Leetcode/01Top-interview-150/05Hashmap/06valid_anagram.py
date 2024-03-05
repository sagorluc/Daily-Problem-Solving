class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_check_freq = {}
        t_check_freq = {}
        
        for char in s:
            s_check_freq[char] = s_check_freq.get(char, 0) + 1
        
        for char in t:
            t_check_freq[char] = t_check_freq.get(char, 0) + 1
            
        if t_check_freq == s_check_freq:
            return True
        else:
            return False    
    
input_str1 = input('Enter an first string: ')
input_str2 = input('Enter an second string: ')
sl = Solution()
res = sl.isAnagram(input_str1, input_str2)
print('is anagram: ', res)
    
