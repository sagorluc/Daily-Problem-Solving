# problem link: https://www.hackerrank.com/contests/ycpc-by-phitron-1st-round-beginner-level-contest-1-2024-1/challenges/spiral-prime

def is_prime(num):
    if num <= 1:
        return False # not prime
    
    # print(int(num**0.5) + 1) # floor value
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False # not prime
        
    return True


def make_primes(N):
    primes = []
    num = 2

    while len(primes) < N:
        if is_prime(num):
            primes.append(num)
        num += 1
        
    return primes


n = int(input('Enter a number.. '))

# make pattern
N = n*n
total_primes = make_primes(N)

# make matrix
index = 0
matrix = [[0] * n for _ in range(n)]
# print(matrix, 'line 37')

for i in range(n):
    if i % 2 == 0: # even row
        for j in range(n):
            matrix[i][j] = total_primes[index]
            index += 1
    else:
        for j in range(n-1, -1, -1): # reverse order for odd row
            matrix[i][j] = total_primes[index]
            index += 1
            
for row in matrix:
    print(' '.join(map(str, row)))
            
