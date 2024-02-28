def countSquares(m,n):
    if m > n:
        return countSquares(n, m)
    elif m == 1:
        return n
    else:
        return (n - m) * (1 + m) * m // 2 + m * (m + 1) * (2 * m + 1) // 6
    
m = int(input())
n = int(input())
print(countSquares(m, n))