
import math


print("--- [1] BMI 비만도 판정 프로그램 ---")
bmi = float(input("체질량지수(BMI)를 입력하세요: "))

if bmi >= 35:
    result = "3단계 비만"
elif 30 <= bmi < 35:
    result = "2단계 비만"
elif 25 <= bmi < 30:
    result = "1단계 비만"
elif 23 <= bmi < 25:
    result = "비만 전단계"
else:
    result = "정상 범위"

print(f"결과: 귀하는 '{result}'에 해당합니다.")
print("-" * 35)


print("\n--- [2] 좌표 사분면 판별 프로그램 ---")
x = int(input("x 좌표를 입력하세요: "))
y = int(input("y 좌표를 입력하세요: "))

if x > 0 and y > 0:
    pos = "1사분면"
elif x < 0 and y > 0:
    pos = "2사분면"
elif x < 0 and y < 0:
    pos = "3사분면"
elif x > 0 and y < 0:
    pos = "4사분면"
else:
    pos = "축(Axis) 위"

print(f"입력한 좌표({x}, {y})는 {pos}입니다.")
print("-" * 35)


print("\n--- [3] 원의 둘레와 면적 계산기 ---")
r = float(input("원의 반지름을 입력하세요: "))

circumference = 2 * math.pi * r
area = math.pi * (r ** 2)

print(f"원의 둘레: {circumference:.1f}")
print(f"원의 면적: {area:.2f}")
print("-" * 35)

print("\n과제가 성공적으로 완료되었습니다.")
