
try:
    N, X, Y = map(int, input().split())
    digits = input().strip()
    if len(digits) != N:
        print("NO")
    else:
        a = int(digits[X - 1])
        b = int(digits[Y - 1])

        if a == 0 or b == 0:
            print("NO")
        elif a % b == 0 or b % a == 0:
            print("YES")
        else:
            print("NO")
except:
    print("NO")