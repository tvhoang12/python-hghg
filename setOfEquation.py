import math

def setOfEquation(numbers):
    a = numbers[0]
    b = numbers[1]
    k = numbers[2]
    m = numbers[3]
    n = numbers[4]
    q = numbers[5]

    det = a*n - b*m
    det_y = a*q - m*k
    det_x = n*k - b*q
    
    if det == 0:
        if det_x == 0 and det_y == 0:
            return "Infinities"
        else:
            return "Can't solve"
    else:
        x = det_x / det
        y = det_y / det
        return str(x) + "," + str(y)n