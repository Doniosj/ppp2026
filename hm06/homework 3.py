# 삼각형의 높이 n을 입력받습니다.
n = int(input("삼각형의 높이(n)를 입력하세요: "))

# 1부터 n까지 반복하며 별을 출력합니다.
for i in range(1, n + 1):
    print("*" * i)