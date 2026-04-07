import math

# 표의 헤더 출력
print(f"{'각도(deg)':>8} | {'sin':>8} | {'cos':>8} | {'tan':>8}")
print("-" * 40)

# 0도부터 90도까지 15도 간격으로 계산
for degree in range(0, 91, 15):
    # 각도를 라디안으로 변환: radian = degree * (pi / 180)
    radian = math.radians(degree)

    s = math.sin(radian)
    c = math.cos(radian)

    # 탄젠트 90도는 무한대이므로 예외 처리
    if degree == 90:
        t = "INF"
    else:
        t = f"{math.tan(radian):.4f}"

    print(f"{degree:8d} | {s:8.4f} | {c:8.4f} | {t:>8}")