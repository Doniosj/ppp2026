def read_weather_data(filename):
    dates = []
    tmax = []
    tmin = []
    tavg = []

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == "":
            continue
        parts = line.split(",")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        dates.append([year, month, day])
        tmax.append(float(parts[3]))
        tmin.append(float(parts[4]))
        tavg.append(float(parts[5]))

    return dates, tmax, tmin, tavg


def get_years(dates):
    years = []
    for date in dates:
        if date[0] not in years:
            years.append(date[0])
    return years


def maximum_temp_gap(dates, tmax, tmin):
    max_gap = tmax[0] - tmin[0]
    max_date = dates[0]

    for i in range(1, len(dates)):
        gap = tmax[i] - tmin[i]
        if gap > max_gap:
            max_gap = gap
            max_date = dates[i]

    return max_date, max_gap


def filter_by_year(dates, tmax, tmin, tavg, year):
    filtered_dates = []
    filtered_tmax = []
    filtered_tmin = []
    filtered_tavg = []

    for i in range(len(dates)):
        if dates[i][0] == year:
            filtered_dates.append(dates[i])
            filtered_tmax.append(tmax[i])
            filtered_tmin.append(tmin[i])
            filtered_tavg.append(tavg[i])

    return filtered_dates, filtered_tmax, filtered_tmin, filtered_tavg


def filter_month(tavg, dates, months):
    filtered = []
    for i in range(len(dates)):
        if dates[i][1] in months:
            filtered.append(tavg[i])
    return filtered


def gdd(temps, base_temp=5):
    total = 0
    for t in temps:
        if t >= base_temp:
            total = total + (t - base_temp)
    return total


dates, tmax, tmin, tavg = read_weather_data("weather_2001_2022.csv")

years = get_years(dates)

print("Task 1: Maximum daily temperature gap per year")
for year in years:
    year_dates, year_tmax, year_tmin, year_tavg = filter_by_year(dates, tmax, tmin, tavg, year)
    max_date, max_gap = maximum_temp_gap(year_dates, year_tmax, year_tmin)
    print(str(max_date[0]) + "/" + str(max_date[1]).zfill(2) + "/" + str(max_date[2]).zfill(2) + "  " + str(
        round(max_gap, 1)))

print()
print("Task 2: Growing Degree Days (May-September) per year")
for year in years:
    year_dates, year_tmax, year_tmin, year_tavg = filter_by_year(dates, tmax, tmin, tavg, year)
    season_temps = filter_month(year_tavg, year_dates, [5, 6, 7, 8, 9])
    total_gdd = gdd(season_temps)
    print(str(year) + "  " + str(round(total_gdd, 1))