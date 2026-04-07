# 마트 상품 사전 {상품명: [가격, 재고]}
mart = {
    "사과": [1500, 10],
    "바나나": [800, 5],
    "우유": [2500, 8],
    "빵": [3000, 3],
    "계란": [6000, 6]
}

print("=== 마트 쇼핑 프로그램 ===")

cart = {}  # 장바구니 {상품명: 수량}
total = 0  # 총 금액

while True:
    print("\n[ 상품 목록 ]")
    print(f"{'상품명':<8} {'가격':>6} {'재고':>5}")
    print("-" * 25)
    for name, (price, stock) in mart.items():
        print(f"{name:<8} {price:>5}원  {stock:>3}개")

    print("\n1. 상품 구매  2. 장바구니 보기  3. 계산 후 종료")
    choice = input("선택: ")

    if choice == "1":
        item = input("구매할 상품명: ")

        if item not in mart:
            print("없는 상품입니다.")
            continue

        qty = int(input("수량: "))
        price, stock = mart[item]

        if qty > stock:
            print(f"재고 부족! (현재 재고: {stock}개)")
            continue

        # 장바구니에 추가 & 재고 차감
        cart[item] = cart.get(item, 0) + qty
        mart[item][1] -= qty
        print(f"{item} {qty}개를 장바구니에 담았습니다.")

    elif choice == "2":
        if not cart:
            print("장바구니가 비어 있습니다.")
        else:
            print("\n[ 장바구니 ]")
            for item, qty in cart.items():
                subtotal = mart[item][0] * qty
                print(f"  {item} x{qty} = {subtotal:,}원")

    elif choice == "3":
        if not cart:
            print("구매한 상품이 없습니다.")
        else:
            print("\n=== 영수증 ===")
            for item, qty in cart.items():
                subtotal = mart[item][0] * qty
                total += subtotal
                print(f"  {item:<8} x{qty}  {subtotal:>7,}원")
            print("-" * 25)
            print(f"  {'합계':<10}  {total:>7,}원")
        break

print("\n이용해 주셔서 감사합니다!")