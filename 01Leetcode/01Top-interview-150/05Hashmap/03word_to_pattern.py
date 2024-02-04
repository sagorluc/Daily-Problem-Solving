class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        make_word = s
        # print(make_word)
        if len(pattern) != len(make_word):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, make_word):
            # print(char, '-->', word)
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            
            char_to_word[char] = word # {'a': 'dog', 'b': 'cat'}
            word_to_char[word] = char # {'dog': 'a', 'cat': 'b'}
            
        # print(char_to_word)
        # print(word_to_char)
        return True
    
    
pattern = input('Enter pattern: ')
word    = input('Enter word: ').split()
sl      = Solution()
res     = sl.wordPattern(pattern, word)
print('Word Pattern: ', res)