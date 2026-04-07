import math
# --- [1] 실습 #03-1: 섭씨를 화씨로 변환 ---
print("--- [1] 섭씨 -> 화씨 변환 ---")
celsius = float(input("섭씨 온도(°C)를 입력하세요: "))
fahrenheit = (celsius * 9/5) + 32
print(f"화씨 온도: {fahrenheit:.2f}°F\n")


# --- [2] 실습 #03-3: BMI(체질량지수) 구하기 ---
print("--- [2] BMI 계산기 ---")
weight = float(input("몸무게(kg)를 입력하세요: "))
height_cm = float(input("키(cm)를 입력하세요: "))
height_m = height_cm / 100 # cm를 m로 변환
bmi = weight / math.pow(height_m, 2)
print(f"당신의 BMI 지수: {bmi:.2f}\n")


# --- [3] 실습 #02-3: 원의 면적 구하기 ---
print("--- [3] 원의 면적 계산 ---")
radius = float(input("원의 반지름을 입력하세요: "))
circle_area = math.pi * math.pow(radius, 2)
print(f"원의 면적: {circle_area:.4f}\n")


# --- [4] 실습 #02-4: 사다리꼴 면적 구하기 ---
print("--- [4] 사다리꼴 면적 계산 ---")
top = float(input("윗변의 길이를 입력하세요: "))
bottom = float(input("밑변의 길이를 입력하세요: "))
height = float(input("높이를 입력하세요: "))
trapezoid_area = (top + bottom) * height / 2
print(f"사다리꼴의 면적: {trapezoid_area:.2f}\n")


# --- [5] 두 지점 사이의 거리 구하기 ---
print("--- [5] 두 지점 사이의 거리 계산 ---")
x1 = float(input("x1 좌표: "))
y1 = float(input("y1 좌표: "))
x2 = float(input("x2 좌표: "))
y2 = float(input("y2 좌표: "))
# 거리 공식: sqrt((x2-x1)^2 + (y2-y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(f"두 지점 사이의 거리: {distance:.4f}\n")


# --- [6] 과일 칼로리 계산하기 ---
print("--- [6] 과일 칼로리 계산 (100g 기준) ---")
# 칼로리 정보 (1g당 칼로리로 환산)
# 한라봉: 50kcal/100g -> 0.5kcal/g
# 딸기: 34kcal/100g -> 0.34kcal/g
# 바나나: 77kcal/100g -> 0.77kcal/g

hallabong_g = float(input("한라봉 섭취량(g)을 입력하세요: "))
strawberry_g = float(input("딸기(설향) 섭취량(g)을 입력하세요: "))
banana_g = float(input("바나나 섭취량(g)을 입력하세요: "))

total_calories = (hallabong_g * 0.5) + (strawberry_g * 0.34) + (banana_g * 0.77)

print(f"\n[결과]")
print(f"한라봉: {hallabong_g * 0.5:.1f} kcal")
print(f"딸기: {strawberry_g * 0.34:.1f} kcal")
print(f"바나나: {banana_g * 0.77:.1f} kcal")
print(f"총 섭취 칼로리: {total_calories:.2f} kcal")