# 1) 칼로리 계산 프로그램
def calorie_calculator():
    calorie_dict = {
        "밥":   130,
        "김치":  15,
        "계란": 155,
        "삼겹살": 331,
        "라면": 450,
        "사과":  52,
        "바나나": 89,
        "콜라":  42
    }

    print("=== 칼로리 계산 프로그램 ===")
    print("등록된 음식:", list(calorie_dict.keys()))

    total_calories = 0
    eaten_foods = []

    while True:
        food = input("\n먹은 음식 입력 (종료: 0): ")
        if food == "0":
            break

        if food in calorie_dict:
            amount = int(input("섭취량(g): "))
            cal = calorie_dict[food] * amount / 100
            total_calories += cal
            eaten_foods.append((food, amount, cal))
            print(f"  → {food} {amount}g = {cal:.1f} kcal")
        else:
            print("  등록되지 않은 음식입니다.")

    print("\n[ 오늘 섭취 요약 ]")
    for food, amount, cal in eaten_foods:
        print(f"  {food} {amount}g : {cal:.1f} kcal")
    print(f"총 칼로리 : {total_calories:.1f} kcal")


# ============================================================
# 2) 구구단 함수
def gugudan(dan):
    print(f"\n=== {dan}단 ===")
    for i in range(1, 10):
        print(f"  {dan} x {i} = {dan * i}")


# ============================================================
# 3) 섭씨 → 화씨 변환 함수
def c2f(t_c):
    t_f = t_c * 9/5 + 32
    return t_f


# ============================================================
# 4) 1부터 n까지의 합
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# ============================================================
# 메인 함수
def main():

    # --- 1) 칼로리 계산 ---
    print("=" * 40)
    print("[1] 칼로리 계산기")
    print("=" * 40)
    calorie_calculator()

    # --- 2) 구구단 ---
    print("\n" + "=" * 40)
    print("[2] 구구단")
    print("=" * 40)
    dan = int(input("구구단 숫자 입력: "))
    gugudan(dan)

    # --- 3) 섭씨 → 화씨 ---
    print("\n" + "=" * 40)
    print("[3] 섭씨 → 화씨 변환")
    print("=" * 40)
    t_c = float(input("섭씨 온도 입력: "))
    t_f = c2f(t_c)
    print(f"  섭씨 {t_c}도 → 화씨 {t_f:.1f}도")

    # --- 4) 1~n 합계 ---
    print("\n" + "=" * 40)
    print("[4] 1부터 n까지의 합")
    print("=" * 40)
    n = int(input("n 입력: "))
    result = sum_n(n)
    print(f"  1 ~ {n} 의 합 = {result}")


# ============================================================
# 프로그램 시작점
if _name_ == "_main_":
    main()