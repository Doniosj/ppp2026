# 음식별 칼로리 사전 (kcal per 100g)
calorie_dict = {
    "밥": 130,
    "김치": 15,
    "계란": 155,
    "삼겹살": 331,
    "라면": 450,
    "사과": 52,
    "바나나": 89,
    "콜라": 42
}

print("=== 칼로리 계산 프로그램 ===")
print("등록된 음식:", list(calorie_dict.keys()))
print()

total_calories = 0
eaten_foods = []

while True:
    food = input("먹은 음식을 입력하세요 (종료: 0): ")

    if food == "0":
        break

    if food in calorie_dict:
        amount = int(input(f"섭취량(g)을 입력하세요: "))
        calories = calorie_dict[food] * amount / 100
        total_calories += calories
        eaten_foods.append((food, amount, calories))
        print(f"  → {food} {amount}g = {calories:.1f} kcal\n")
    else:
        print("  등록되지 않은 음식입니다.\n")

print("\n=== 오늘 섭취 요약 ===")
for food, amount, cal in eaten_foods:
    print(f"  {food} {amount}g : {cal:.1f} kcal")
print(f"\n총 칼로리: {total_calories:.1f} kcal")

if total_calories < 1500:
    print("칼로리가 부족합니다. 더 드세요!")
elif total_calories <= 2500:
    print("적정 칼로리입니다. 잘 드셨어요!")
else:
    print("칼로리가 초과되었습니다. 주의하세요!")