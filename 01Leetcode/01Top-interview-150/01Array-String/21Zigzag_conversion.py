class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_str = len(s)
        
        if numRows == 1 or numRows >= len_str:
            return s
            
        rows = [[] for row in range(numRows)] # 2d array
        index = 0
        step = -1
        
        for char in s:
            rows[index].append(char)
            # print(rows[index])
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1               
            
            index = index + step
            # print(index)
                
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
            
        return ''.join(rows)
                
        
input_str = input("Enter a string: ")
input_row = int(input("Enter a number of row: "))
sl = Solution()
res = sl.convert(input_str, input_row)
print("The zigzag string is ", res)