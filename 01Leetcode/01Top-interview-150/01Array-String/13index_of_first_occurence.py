class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(haystack)
        b = len(needle)
        rest = a - b
        ans = -1
        for i in range(rest+1):
            # print(haystack[i:i + len_n]) # sad
            if haystack[i:i + b] == needle:
               return i                      
        return ans        
        
        # len_n = len(needle)
        # min_len = min(len(haystack), len_n)
        # # print(min_len)
        # ans = -1
        # for i in range(min_len+1):
        #     # print(haystack[i:i + len_n]) # sad
        #     if haystack[i:i + len_n] == needle:
        #        return i
        #     else:
        #         return -1
            
        
            
            
input_haystack = input('Enter haystack: ') # sadbutsad
input_needle = input('Enter needle: ')     # sad

sl = Solution()
res = sl.strStr(input_haystack, input_needle)
print('Index is:', res)