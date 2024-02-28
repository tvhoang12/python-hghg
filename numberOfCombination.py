import math

n = int(input())
m = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, m):
    return factorial(n) / (factorial(m) * factorial(n-m))

print(math.comb(n, m))