class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sp_str = strs.split()
        sp_str = sorted(sp_str)
        # print(sp_str)
        first = sp_str[0]
        last = sp_str[-1]
        min_len = min(len(first), len(last))
       
        new_str = ""
        for i in range(min_len):
            if first[i] == last[i]:
                new_str += first[i]
            else:
                return new_str
        return new_str
                
        
    
input_str = input('Enter the sentence: ').lower()
sl = Solution()
res = sl.longestCommonPrefix(input_str)
print('Longest common prefix is: ', res)
    
    
    