import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'Malgun Gothic'

df146 = pd.read_csv("weather_146__1980-2024.csv", skipinitialspace=True)
df119 = pd.read_csv("weather_119__1980-2024.csv", skipinitialspace=True)

# Q1. Jeonju 2012 annual rainfall
rain_2012 = df146[df146['year'] == 2012]['rainfall'].sum()
print(f"Q1. Jeonju 2012 annual rainfall: {rain_2012:.1f} mm")

# Q2. Jeonju 2024 max temperature
tmax_2024 = df146[df146['year'] == 2024]['tmax'].max()
print(f"Q2. Jeonju 2024 max temperature: {tmax_2024:.1f} C")

# Q3. Jeonju 2020 max daily temperature range
df2020 = df146[df146['year'] == 2020].copy()
df2020['range'] = df2020['tmax'] - df2020['tmin']
max_range = df2020['range'].max()
max_day = df2020.loc[df2020['range'].idxmax()]
print(f"Q3. Jeonju 2020 max daily range: {max_range:.1f} C ({int(max_day['month'])}/{int(max_day['day'])})")

# Q4. Rainfall difference between Suwon and Jeonju in 2019
rain_146 = df146[df146['year'] == 2019]['rainfall'].sum()
rain_119 = df119[df119['year'] == 2019]['rainfall'].sum()
print(f"Q4. Jeonju 2019: {rain_146:.1f} mm, Suwon 2019: {rain_119:.1f} mm, Difference: {abs(rain_146 - rain_119):.1f} mm")

# Q5. Line graph average temperature Jeonju and Suwon 1980-2024
avg_146 = df146.groupby('year')['tavg'].mean()
avg_119 = df119.groupby('year')['tavg'].mean()

plt.figure(figsize=(12, 5))
plt.plot(avg_146.index, avg_146.values, marker='o', markersize=3, label='Jeonju (146)', color='red')
plt.plot(avg_119.index, avg_119.values, marker='s', markersize=3, label='Suwon (119)', color='blue')
plt.title('Annual Average Temperature: Jeonju vs Suwon (1980-2024)')
plt.xlabel('Year')
plt.ylabel('Temperature (C)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('q5_avg_temp.png')
plt.show()

# Q6. Bar graph annual rainfall Jeonju 1980-2024
rain_yearly = df146.groupby('year')['rainfall'].sum()

plt.figure(figsize=(14, 5))
plt.bar(rain_yearly.index, rain_yearly.values, color='steelblue')
plt.title('Annual Rainfall: Jeonju (146) 1980-2024')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('q6_rainfall.png')
plt.show()

# Q7. Birthday temperature analysis
birth_month = 9
birth_day = 15
birth_year = 2003

bday = df146[(df146['month'] == birth_month) & (df146['day'] == birth_day)].copy()

plt.figure(figsize=(12, 5))
plt.plot(bday['year'], bday['tavg'], marker='o', markersize=4, label='Avg Temp', color='purple')
plt.plot(bday['year'], bday['tmax'], marker='^', markersize=3, label='Max Temp', color='red', alpha=0.7)
plt.plot(bday['year'], bday['tmin'], marker='v', markersize=3, label='Min Temp', color='blue', alpha=0.7)
plt.axvline(birth_year, color='orange', linestyle='--', label=f'Birth year ({birth_year})')
plt.title(f'Temperature on {birth_month}/{birth_day} each year - Jeonju (146)')
plt.xlabel('Year')
plt.ylabel('Temperature (C)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('q7_birthday.png')
plt.show()

range_data = bday[(bday['year'] >= 1980) & (bday['year'] <= 2014)].copy()
range_data = range_data.sort_values('tavg', ascending=False).reset_index(drop=True)

rank = range_data[range_data['year'] == birth_year].index[0] + 1
hottest = range_data.iloc[0]
coldest = range_data.iloc[-1]

print(f"Q7. {birth_month}/{birth_day} temperature ranking among 1980-2014")
print(f"    Birth year {birth_year} ranks #{rank} warmest")
print(f"    Hottest year: {int(hottest['year'])} ({hottest['tavg']:.1f} C)")
print(f"    Coldest year: {int(coldest['year'])} ({coldest['tavg']:.1f} C)")