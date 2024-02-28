def rotateTable(a,b,c,d):
    maxi = max(a/c - b/d, c/d - a/b ,d/b - c/a, b/a - d/c)
    if maxi == a/c - b/d:
        print(0)
    elif maxi == c/d - a/b:
        print(1)
    elif maxi == d/b - c/a:
        print(2)
    else:
        print(3)

def rotatTable(a,b,c,d):
    rotations = [a/c-b/d, c/d-a/b, d/b-c/a, b/a-d/c]
    return rotations.index(max(rotations))

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(rotatTable(a,b,c,d))