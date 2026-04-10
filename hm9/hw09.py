# 1) 평균을 구하는 함수
def average(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)


# 2) 1~n 리스트를 반환하는 함수
def get_range_list(n):
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result


# 3) 윤년 판별 함수
def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            return False   # 100으로 나누어 떨어지면 윤년 아님
        return True        # 4로 나누어 떨어지면 윤년
    return False           # 4로 나누어 떨어지지 않으면 윤년 아님


# 4) split()으로 여러 값 입력받아 평균 출력
def average_from_input():
    user_input = input("숫자를 공백으로 입력하세요 (예: 10 20 30): ")
    nums = list(map(int, user_input.split()))
    result = average(nums)   # 1번 함수 재사용
    print(f"입력한 숫자: {nums}")
    print(f"평균: {result:.2f}")


# ============================================================
# 메인 함수 - import 시 자동 실행 방지
# ============================================================
def main():

    # --- 1) 평균 ---
    print("=" * 40)
    print("[1] 평균 계산 - average(nums)")
    print("=" * 40)
    nums = [10, 20, 30, 40, 50]
    print(f"리스트: {nums}")
    print(f"평균  : {average(nums):.2f}")


    # --- 2) 1~n 리스트 ---
    print("\n" + "=" * 40)
    print("[2] 1~n 리스트 - get_range_list(n)")
    print("=" * 40)
    n = int(input("n을 입력하세요: "))
    print(f"1~{n} 리스트: {get_range_list(n)}")


    # --- 3) 윤년 판별 ---
    print("\n" + "=" * 40)
    print("[3] 윤년 판별 - is_leap_year(y)")
    print("=" * 40)
    test_years = [2000, 1900, 2024, 2023]
    for y in test_years:
        result = is_leap_year(y)
        print(f"  {y}년 → {'윤년 ✓' if result else '윤년 아님 ✗'}")


    # --- 4) 입력받아 평균 ---
    print("\n" + "=" * 40)
    print("[4] 한 줄 입력 평균 - split() 활용")
    print("=" * 40)
    average_from_input()


# ============================================================
# import 시 main() 실행 방지
# ============================================================
if _name_ == "_main_":
    main()