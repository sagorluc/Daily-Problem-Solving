
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        st = 0
        last = len(numbers) -1
        
        for i in range(len(numbers)):
            if numbers[st] + numbers[last] == target:
                return [st+1, last+1]
            
            elif numbers[st] + numbers[last] > target:
                last -= 1
            else:
                st += 1
       
input_arr = list(map(int, input("Enter an array: ").split()))
input_num = int(input('Enter a number: '))
sort_arr = sorted(input_arr)
sl = Solution()
res = sl.twoSum(input_arr, input_num)
print("Index is: ", res)




# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         st = 0
#         last = len(numbers)-1
        
#         for i in range(len(numbers)):
#             if numbers[st] + numbers[last] == target:
#                 return [st+1, last+1]
            
#             elif numbers[st] + numbers[last] > target:
#                 last -= 1
#             else:
#                 st += 1
            
               
# input_arr = list(map(int, input("Enter an array: ").split()))
# input_num = int(input("Enter a number: "))
# sort_arr = sorted(input_arr)
# sl = Solution()
# res = sl.twoSum(sort_arr, input_num)
# print('The target sum of index is', res)