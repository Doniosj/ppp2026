import random

WORD_LIST = [
    "python", "programming", "computer", "keyboard",
    "algorithm", "variable", "function", "university"
]

def hangman():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    trials = 7
    wrong_guesses = []

    print("=" * 30)
    print("       Hangman Game!")
    print("=" * 30)

    while trials > 0 and "_" in display:
        print(f"\n  Word:   {' '.join(display)}")
        print(f"  Trials: {trials}")
        print(f"  Wrong:  {', '.join(wrong_guesses) if wrong_guesses else '-'}")

        guess = input("  Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("  Please enter a single letter!")
            continue

        if guess in wrong_guesses or guess in display:
            print("  Already guessed that letter!")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    display[i] = guess
            print("  Correct!")
        else:
            wrong_guesses.append(guess)
            trials -= 1
            print(f"  Wrong! {trials} trials left.")

    print("\n" + "=" * 30)
    if "_" not in display:
        print(f"  You win! The word was: {answer}")
    else:
        print(f"  Game over! The word was: {answer}")
    print("=" * 30)

hangman()