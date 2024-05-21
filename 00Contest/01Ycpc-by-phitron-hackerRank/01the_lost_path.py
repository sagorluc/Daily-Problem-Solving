# problem link: https://www.hackerrank.com/contests/ycpc-by-phitron-1st-round-beginner-level-contest-1-2024-1/challenges/the-lost-path

if __name__ == '__main__':
    inputs = input().split()  # Read numbers a and b separated by space
    path_a = int(inputs[0])
    path_b = int(inputs[1])

    if path_b == 0:
        print(-1)
    else:
        print(path_a % path_b)
        
        
# if __name__ == '__main__':
#     # path_a = int(input('Enter number a: '))
#     # path_b = int(input('Enter number b: '))
#     inputs = input().split() # Enter numbers a and b separated by space
#     path_a = int(inputs[0])
#     path_b = int(inputs[1])

#     if path_b == 0 or path_b * path_a > path_a or path_b > path_a:
#         print(-1)
#     elif path_a % path_b != 0:
#         ans = path_a / path_b
#         print(ans)
#     else:
#         print(-1)

    