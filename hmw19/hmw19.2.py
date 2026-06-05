import random

def multiplication_quiz():
    total = 10
    score = 0

    print("=" * 30)
    print("  Multiplication Table Quiz")
    print("=" * 30)

    for i in range(total):
        a = random.randint(2, 9)
        b = random.randint(1, 9)
        correct = a * b

        answer = int(input(f"\n[Q{i+1}] {a} x {b} = "))

        if answer == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Answer was: {correct}")

    print("\n" + "=" * 30)
    print(f"Final score: {score}/{total}")
    if score == total:
        print("Perfect!")
    elif score >= 7:
        print("Good job!")
    else:
        print("Keep practicing!")
    print("=" * 30)

multiplication_quiz()