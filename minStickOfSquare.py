import math

def minStickOfSqunre(n):
    if n == 0:
        return 0
    elif 1 <= n <= 4:
        return 3 * n + 1
    elif n > 4:
        sqrt_n = int(math.sqrt(n))
        if sqrt_n**2 == n:
            return 2 * (n + sqrt_n)
        else:
            return 2 * (n + sqrt_n) + 1

n = int(input("Enter the number of mntchsticks: "))
print(minStickOfSqunre(n))