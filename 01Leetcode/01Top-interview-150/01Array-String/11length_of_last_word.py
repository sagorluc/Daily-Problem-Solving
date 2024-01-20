class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        # print(a[-1], 'line 4')
        last_word = a[-1]
        len_of_last_word = len(last_word)
        # print(len_of_last_word)
        return len_of_last_word
    

input_str = input('Enter an sentence: ')   
sl = Solution()
res = sl.lengthOfLastWord(input_str)
print('Length of last word: ', res)


# Remove duplicate email
# my_list = ['def274753@gmail.com', 'django712345@protonmail.com', ['def274753@gmail.com', 'django712345@protonmail.com', 'kitewo8201@tsderp.com']]

# # Initialize a set to keep track of seen elements
# seen_elements = set()

# # Initialize a new list to store unique elements
# unique_list = []

# for element in my_list:
#     # Check if the element is a list
#     if isinstance(element, list):
#         # If it's a list, iterate over its elements
#         for nested_element in element:
#             # Add each unique element to the set and the new list
#             if nested_element not in seen_elements:
#                 seen_elements.add(nested_element)
#                 unique_list.append(nested_element)
#     else:
#         # If it's not a list, add it to the set and the new list
#         if element not in seen_elements:
#             seen_elements.add(element)
#             unique_list.append(element)

# print(unique_list)