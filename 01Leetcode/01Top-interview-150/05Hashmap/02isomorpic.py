class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []
        
        for idx in s:
            map1.append(s.index(idx))
            # print(map1)
        for idx in t:
            map2.append(t.index(idx))
            # print(map2)
        # print(map1, 'line 9')  # [0, 1, 1]
        # print(map2, 'line 13') # [0, 1, 2]
        
        if map1 == map2:
            return True
        else:
            return False
        
    
input_str = input("Enter first sentence: ")
input_str1= input("Enter second sentence: ")

sl = Solution()
res = sl.isIsomorphic(input_str, input_str1)
print("Can Construct: ", res)