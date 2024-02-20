import math

t = int(input())
lst = list(map(int, input().split()))
lst.sort()

for i in range(t - 1):
    for j in range(i + 1, t):
        if math.gcd(lst[i], lst[j]) == 1:
            print(lst[i], lst[j], sep = " ")