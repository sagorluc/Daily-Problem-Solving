class Solution:
    def maxArea(self, height: list[int]) -> int:
        st = 0
        last = len(height)-1
        print(last)
        print(height[last])
        max_area = 0
        
        while st < last:
            cur_area = min(height[st], height[last]) * (last - st)
            print(cur_area)
            max_area = max(max_area, cur_area)
            
            if height[st] < height[last]:
                st += 1
            else:
                last -= 1
        return max_area
        
    

new_arr = []   
input_num = int(input("Enter a number: "))
input_arr = list(map(int, input("Enter an array: ").split())) # [1,8,6,2,5,4,8,3,7]

for i in range(input_num):
    val = input_arr[i]
    new_arr.append(val)
    
# print(new_arr)
# sort_arr = sorted(new_arr)
sl = Solution()
res = sl.maxArea(new_arr)
print("Container with most water: ",res)