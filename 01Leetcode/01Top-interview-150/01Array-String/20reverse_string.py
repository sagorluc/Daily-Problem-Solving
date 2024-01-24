class Solution:
    def reverseWords(self, s: str):
        # rev_str = reversed(s)
        rev_str = s[::-1]
        return ' '.join(rev_str)
    
    
input_str = input("Enter the sentence of word: ")
sp_str = input_str.split() # make the array
sl = Solution()
res = sl.reverseWords(sp_str)
print("The reverse string is ", res)