class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        target = 0
        last = len(nums)-1
        distinct = set()
        tiplet = []
        
        if len(nums) >= 3:
            for i in range(len(nums)):
                j = i+1
                k = last
                while j < k:
                    sum3 = nums[i] + nums[j] + nums[k]
                    
                    if sum3 == target:
                        distinct.add((nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1
                    elif sum3 < target:
                        j += 1
                    else:
                        k -= 1
            tiplet = list(distinct)
            # tiplet.append(output)
            # print(tiplet)
            return tiplet
                    


    
new_arr = []   
input_num = int(input("Enter a number: "))
input_arr = list(map(int, input("Enter an array: ").split())) # [-1,0,1,2,-1,-4]

for i in range(input_num):
    val = input_arr[i]
    new_arr.append(val)
    
# print(new_arr)
# sort_arr = sorted(new_arr)
sl = Solution()
res = sl.threeSum(new_arr)
print("3 sum triplets: ",res)