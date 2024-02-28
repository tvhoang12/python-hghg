def angle_hands_clock(h,m):
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    
    return int(min(abs(hour_angle - minute_angle), 360 - abs(hour_angle - minute_angle)))

if __name__ == "__main__":
    h = int(input())
    m = int(input())
    print(angle_hands_clock(h,m))