class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        ans = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            ans = max(ans, right - left + 1)
            
        return ans
            
    
    
input_str = input('Enter an string: ')
sl = Solution()
res = sl.lengthOfLongestSubstring(input_str)
print('Length of substring is: ', res)