class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       lst = list(s)
       # print(lst)
       len_s = len(lst)
       ans = 0
       
       for char in t:
           try:
            if char == lst[ans]:
                ans += 1
           except:
               continue
        
       if ans == len_s:
           return True
       else:
           return False
       
                   
input_str = input("Enter an string: ").lower()
input_str2 = input("Enter an string2: ").lower()

sl = Solution()
res = sl.isSubsequence(input_str, input_str2)
print('Is Subsequence: ', res)
