def read_weather_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        header = f.readline()  # 첫 줄은 헤더라서 그냥 넘김
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


def calc_annual_avg_temp(data):
    total = 0
    count = 0
    for row in data:
        total += row['tavg']
        count += 1
    if count == 0:
        return 0
    return total / count


def calc_rainy_days(data, threshold=5.0):
    count = 0
    for row in data:
        if row['rainfall'] >= threshold:
            count += 1
    return count


def calc_total_rainfall(data):
    total = 0
    for row in data:
        total += row['rainfall']
    return total


def main():
    filename = 'weather(146)_2022-2022.csv'

    data = read_weather_data(filename)

    avg_temp    = calc_annual_avg_temp(data)
    rainy_days  = calc_rainy_days(data, threshold=5.0)
    total_rain  = calc_total_rainfall(data)

    print(f'연 평균 기온    : {avg_temp:.2f} °C')
    print(f'5mm 이상 강우일수: {rainy_days} 일')
    print(f'총 강우량       : {total_rain:.1f} mm')


if _name_ == '_main_':
    main()