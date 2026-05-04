def read_weather_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            line = line.strip()
            if line == '':
                continue
            parts = line.split(',')
            row = {
                'year':     int(parts[0]),
                'month':    int(parts[1]),
                'day':      int(parts[2]),
                'tmax':     float(parts[3]),
                'tavg':     float(parts[4]),
                'tmin':     float(parts[5]),
                'humid':    float(parts[6]),
                'wind':     float(parts[7]),
                'sunshine': float(parts[8]),
                'rainfall': float(parts[9]),
                'snow':     float(parts[10]),
                'cloud':    float(parts[11]),
            }
            data.append(row)
    return data


def max_consecutive_rain_days(data):
    max_streak = 0
    current_streak = 0

    for row in data:
        if row['rainfall'] > 0:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        else:
            current_streak = 0

    return max_streak


def max_rain_event(data):
    events = []
    current_total = 0
    in_rain = False

    for row in data:
        if row['rainfall'] > 0:
            current_total += row['rainfall']
            in_rain = True
        else:
            if in_rain:
                events.append(current_total)
                current_total = 0
                in_rain = False

    if in_rain:
        events.append(current_total)

    if len(events) == 0:
        return 0

    max_event = 0
    for e in events:
        if e > max_event:
            max_event = e

    return max_event


def top3_hottest_days(data):
    sorted_data = []

    for row in data:
        sorted_data.append(row)

    n = len(sorted_data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sorted_data[j]['tmax'] < sorted_data[j + 1]['tmax']:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]

    top3 = sorted_data[:3]
    return top3


def main():
    filename = 'weather(146)_2022-2022.csv'

    data = read_weather_data(filename)

    max_streak = max_consecutive_rain_days(data)
    print(f'4) 최장 연속 강우일수: {max_streak} 일')

    max_event_rain = max_rain_event(data)
    print(f'5) 강우 이벤트 중 최대 강수량: {max_event_rain:.1f} mm')

    top3 = top3_hottest_days(data)
    print('6) 가장 더운날 Top 3:')
    rank = 1
    for day in top3:
        print(f'   {rank}위: {day["year"]}년 {day["month"]}월 {day["day"]}일 - tmax {day["tmax"]}°C')
        rank += 1


if _name_ == '_main_':
    main()