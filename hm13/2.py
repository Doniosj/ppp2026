filename = "weather(146)_2001-2022.csv"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")

date_col = header.index("날짜")
rain_col = header.index("일강수량(mm)")

total_2021 = 0.0
total_2022 = 0.0

for line in lines[1:]:
    parts = line.strip().split(",")

    date_str = parts[date_col]
    rain_str = parts[rain_col]

    year = int(date_str.split("-")[0])

    if year not in [2021, 2022]:
        continue

    if rain_str.strip() == "" or rain_str.strip() == "-":
        rainfall = 0.0
    else:
        rainfall = float(rain_str)

    if year == 2021:
        total_2021 = total_2021 + rainfall
    else:
        total_2022 = total_2022 + rainfall

print("Total rainfall in 2021: %.1f mm" % total_2021)
print("Total rainfall in 2022: %.1f mm" % total_2022)