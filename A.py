A, B = map(int, input().split())


def sumOfDigits(x: int):
    sum = 0
    while True:
        sum += x % 10
        x = x // 10
        if x == 0:
            break
    return sum


print(max(sumOfDigits(A), sumOfDigits(B)))
