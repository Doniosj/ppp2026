# 1) 섭씨 → 화씨 변환
# 공식: F = C × 9/5 + 32

celsius1 = 30
celsius2 = 0

fahrenheit1 = celsius1 * 9/5 + 32
fahrenheit2 = celsius2 * 9/5 + 32

print("=== 1) 섭씨 → 화씨 변환 ===")
print(f"섭씨 {celsius1}도 → 화씨 {fahrenheit1}도")
print(f"섭씨 {celsius2}도 → 화씨 {fahrenheit2}도")


# 2) BMI 계산
# 공식: BMI = 몸무게(kg) / 키(m)²

print("\n=== 2) BMI 계산 ===")
weight = 70      # kg
height = 1.75    # m

bmi = weight / (height ** 2)
print(f"키: {height}m, 몸무게: {weight}kg")
print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
    print("판정: 저체중")
elif bmi < 23:
    print("판정: 정상")
elif bmi < 25:
    print("판정: 과체중")
else:
    print("판정: 비만")


# 3) 원의 넓이
# 공식: S = π × r²

print("\n=== 3) 원의 넓이 ===")
PI = 3.14159
r = 4

area = PI * r ** 2
print(f"반지름: {r}")
print(f"원의 넓이 = {area:.2f}")


# 4) 사다리꼴 넓이
# 공식: S = (윗변 + 밑변) × 높이 / 2

print("\n=== 4) 사다리꼴 넓이 ===")
bottom = 5   # 밑변
top    = 3   # 윗변
height = 4   # 높이

area = (top + bottom) * height / 2
print(f"밑변: {bottom}, 윗변: {top}, 높이: {height}")
print(f"사다리꼴 넓이 = {area}")


# 5) 할인 가격 계산

print("\n=== 5) 할인 가격 ===")
price    = 2000   # 원래 가격
discount = 0.15   # 15%

sale_price = price * (1 - discount)
print(f"원래 가격: {price}원")
print(f"할인율: {int(discount*100)}%")
print(f"할인 금액: {int(price * discount)}원")
print(f"최종 가격: {int(sale_price)}원")