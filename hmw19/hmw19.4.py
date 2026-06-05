import random

def generate_lotto():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def lotto_machine():
    print("=" * 30)
    print("   Lotto Number Generator")
    print("=" * 30)

    rounds = int(input("How many rounds? "))

    print()
    for i in range(rounds):
        numbers = generate_lotto()
        formatted = "  ".join(f"{n:2d}" for n in numbers)
        print(f"  Round {i+1}: [ {formatted} ]")

    print("=" * 30)
    print("Good luck!")
    print("=" * 30)

lotto_machine()