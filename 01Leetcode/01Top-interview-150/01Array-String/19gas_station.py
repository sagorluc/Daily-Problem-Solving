class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        len_gas_station = len(gas)
        total = 0
        total2 = 0
        start_index = 0
        
        for i in range(len_gas_station):
            sub_total = gas[i] - cost[i]
            # print(sub_total) # -2 -2 -2 3 3
            total  = total + sub_total 
            total2 = total2 + sub_total
            # print(total, total1) # -2 -4 -6 -3 0
            
            if total2 < 0:
                total2 = 0
                start_index = i + 1
                
        if total < 0:
            return -1
        else: 
            return start_index
                
            
    
    
input_gas = list(map(int, input("Enter an array: ").split())) # 1 2 3 4 5
input_cost = list(map(int, input("Enter an array: ").split())) # 3 4 5 1 2

sl = Solution()
res = sl.canCompleteCircuit(input_gas, input_cost)
print('Start from index: ', res)