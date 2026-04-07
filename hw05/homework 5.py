print("--- 변환 프로그램 메뉴 ---")
print("1. 화씨(°F) -> 섭씨(°C)")
print("2. 섭씨(°C) -> 화씨(°F)")
print("3. 피트(ft) -> 센티미터(cm)")
print("4. 센티미터(cm) -> 피트(ft)")
print("-" * 25)

choice = input("원하는 변환의 번호를 선택하세요: ")

if choice == '1':
    f_temp = float(input("화씨 온도(°F)를 입력하세요: "))
    c_temp = (f_temp - 32) * 5 / 9
    print(f"변환 결과: {c_temp:.1f}°C")

elif choice == '2':
    c_temp = float(input("섭씨 온도(°C)를 입력하세요: "))
    f_temp = (c_temp * 9 / 5) + 32
    print(f"변환 결과: {f_temp:.1f}°F")

elif choice == '3':
    ft = float(input("길이(ft)를 입력하세요: "))
    cm = ft * 30.48
    print(f"변환 결과: {cm:.1f}cm")

elif choice == '4':
    cm = float(input("길이(cm)를 입력하세요: "))
    ft = cm / 30.48
    print(f"변환 결과: {ft:.1f}ft")

else:
    print("잘못된 선택입니다. 1~4 사이의 숫자를 입력해주세요.")