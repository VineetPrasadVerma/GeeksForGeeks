t = int(input())
for _ in range(t):
    hour, minute = tuple(map(int, input().split()))
    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 60
    angle_by_hour_hand = (hour*60 + minute) * 0.5
    angle_by_minute_hand = minute * 6

    print(min(abs(angle_by_hour_hand - angle_by_minute_hand), 360 - abs(angle_by_hour_hand - angle_by_minute_hand)))
