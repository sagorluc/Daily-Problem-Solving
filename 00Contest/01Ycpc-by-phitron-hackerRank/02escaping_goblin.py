
inputs = input('Enter input A and B. ').split()
input_a = inputs[0]
input_b = inputs[1]

input_k = int(input('Enter K. '))

input_a = int(input_a)
input_b = int(input_b)
# input_a = int(input_a)
a = input_a + input_k
b = input_b + input_k
# print('A is= ',input_a, 'B is= ', input_b, 'K is= ', input_k)
if input_k <= 0:
    print('YES')
if (input_a + input_k) < input_b:
    print('YES')
elif (input_b + input_k) < input_a:
    print('YES')
else:
    print('NO')
