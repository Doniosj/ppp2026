import os
import requests

url = "https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
csv_filename = "./weather_146_2023.csv"
output_filename = "./weather_summary_2023.txt"

if not os.path.exists(csv_filename):
    response = requests.get(url)
    response.encoding = "UTF-8"
    with open(csv_filename, "w", encoding="UTF-8-sig") as f:
        f.write(response.text)

total_temp = 0.0
temp_count = 0
rain_days_5mm = 0
total_rainfall = 0.0

with open(csv_filename, "r", encoding="UTF-8-sig") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")

try:
    date_idx = header.index("date")
except ValueError:
    date_idx = 0

try:
    avg_temp_idx = header.index("avg_temp")
except ValueError:
    avg_temp_idx = 1

try:
    rainfall_idx = header.index("rainfall")
except ValueError:
    rainfall_idx = 2

for line in lines[1:]:
    if not line.strip():
        continue

    tokens = line.strip().split(",")
    if len(tokens) <= max(avg_temp_idx, rainfall_idx):
        continue

    try:
        avg_temp = float(tokens[avg_temp_idx])
        total_temp += avg_temp
        temp_count += 1
    except ValueError:
        pass

    try:
        rainfall = float(tokens[rainfall_idx])
        total_rainfall += rainfall
        if rainfall >= 5.0:
            rain_days_5mm += 1
    except ValueError:
        pass

annual_avg_temp = total_temp / temp_count if temp_count > 0 else 0.0

with open(output_filename, "w", encoding="UTF-8") as fout:
    fout.write(f"1) Annual Average Temperature: {annual_avg_temp:.2f}\n")
    fout.write(f"2) Number of Days with Rainfall >= 5mm: {rain_days_5mm} days\n")
    fout.write(f"3) Total Rainfall: {total_rainfall:.2f} mm\n")