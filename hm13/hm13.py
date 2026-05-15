filename = "weather(146)_2022-2022.csv"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")

date_col = header.index("날짜")
rain_col = header.index("일강수량(mm)")

summer_total = 0.0

for line in lines[1:]:
    parts = line.strip().split(",")

    date_str = parts[date_col]
    rain_str = parts[rain_col]

    month = int(date_str.split("-")[1])

    if month not in [6, 7, 8]:
        continue

    if rain_str.strip() == "" or rain_str.strip() == "-":
        rainfall = 0.0
    else:
        rainfall = float(rain_str)

    summer_total = summer_total + rainfall

print("Summer (June - August) total rainfall: %.1f mm" % summer_total)



