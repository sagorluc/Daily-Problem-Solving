
new_arr = []
input_num = int(input('Enter a number: ')) # 17
input_arr = list(map(int, input("Enter an array: ").split())) # [4 1 2 5 6 7 4 2 5 2 1 2 7 6 7 6 7]
ans = 0
occur_dict = {}
for i in range(input_num):
    elem = input_arr[i]
    new_arr.append(elem)
    
    if elem in occur_dict:
        occur_dict[elem] += 1
    else:
        occur_dict[elem] = 1
        
for key, value in occur_dict.items():
    print(key, value)
    if value % 2 != 0:
        ans = key
        break
        
print(occur_dict) # {4: 2, 1: 2, 2: 4, 5: 2, 6: 3, 7: 4}
print(ans)
        
        
# N = 17
# A = [4, 1, 2, 5, 6, 7, 4, 2, 5, 2, 1, 2, 7, 6, 7, 6, 7]
# result = 0
# # XOR all the numbers in the list
# for num in A:
#     result ^= num
# print(result)
