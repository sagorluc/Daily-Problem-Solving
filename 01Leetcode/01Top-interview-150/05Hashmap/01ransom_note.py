class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for char in magazine:
            if char not in  dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
                
        for char1 in ransomNote:
            if char1 in dictionary and dictionary[char1] > 0:
                dictionary[char1] -= 1
            else:
                return False
        
        return True                
                
    
input_str = input("Enter first sentence: ")
input_str1= input("Enter second sentence: ")

sl = Solution()
res = sl.canConstruct(input_str, input_str1)
print("Can Construct: ", res)