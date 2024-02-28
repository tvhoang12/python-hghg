def riverCrossing(n , k):
    if k == 1 or k == 0:
        return 1
    elif k >= n:
        return 1
    elif (n - 1) % (k - 1) == 0:
        return ((n - 1) / (k - 1)) * 2 - 1
    else:
        return ((n - 1) // (k - 1)) * 2 + 1
    
n = int(input())
k = int(input())
print(riverCrossing(n, k))    