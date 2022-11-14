import math


def isPrime(num:int) -> bool:
    if num == 1:
        return False

    end = int(math.sqrt(num))
    for i in range(2, end+1):
        if num % i == 0:
            return False
    return True


def getNumberOfPrime(a:int, b:int) -> int:
    count = 0
    for i in range(a, b):
        if isPrime(i):
            count += 1
    return count


n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))
    print(getNumberOfPrime(a, b))

