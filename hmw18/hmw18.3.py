import random

CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
    'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

WORD_LIST = [
    "사과", "바나나", "컴퓨터", "프로그래밍",
    "전북대학교", "파이썬", "인공지능", "데이터",
    "알고리즘", "소프트웨어"
]


def get_chosung(word: str) -> str:
    result = ""
    for ch in word:
        code = ord(ch)
        if 0xAC00 <= code <= 0xD7A3:
            idx = (code - 0xAC00) // (21 * 28)
            result += CHOSUNG_LIST[idx]
        else:
            result += ch
    return result


def play_chosung_game():
    score = 0
    total = 5

    print("=" * 30)
    print("   Chosung Game Start!")
    print("=" * 30)

    for i in range(total):
        answer = random.choice(WORD_LIST)
        chosung = get_chosung(answer)

        print(f"\n[Question {i + 1}/{total}]")
        print(f"Chosung hint: {chosung}")
        print(f"Word length:  {len(answer)} letters")

        user_input = input("Your answer: ").strip()

        if user_input == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was: {answer}")

    print("\n" + "=" * 30)
    print(f"Game Over! Final score: {score}/{total}")
    if score == total:
        print("Perfect score!")
    elif score >= total // 2:
        print("Good job!")
    else:
        print("Keep practicing!")
    print("=" * 30)


play_chosung_game()