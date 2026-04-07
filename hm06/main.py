# 숫자를 입력받습니다.
num = int(input("출력할 구구단의 숫자를 입력하세요: "))

# 반복문을 사용하여 구구단을 출력합니다.
print(f"--- {num}단 ---")
for i in range(1, 10):
    print(f"{num} * {i} = {num * i}")