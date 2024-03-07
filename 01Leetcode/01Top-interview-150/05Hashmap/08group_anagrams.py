# defaultdict(<class 'list'>, {})
# aet line 9
# defaultdict(<class 'list'>, {'aet': ['eat']}) line 11
# aet line 9
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea']}) line 11
# ant line 9
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea'], 'ant': ['tan']}) line 11
# aet line 9
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']}) line 11
# ant line 9
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat']}) line 11
# abt line 9
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}) line 11    
# Group Anagrame:  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]



from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        print(anagram_map)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            print(sorted_word, 'line 9')       # aet, aet, ant, aet, ant, abt
            anagram_map[sorted_word].append(word)
            print(anagram_map, 'line 11')
        
        return list(anagram_map.values())
        
    
input_arr = input('Enter an string of array: ') # eat tea tan ate nat bat
spl_arr = input_arr.split(' ')
sl = Solution()
res = sl.groupAnagrams(spl_arr)
print('Group Anagrame: ', res)