import time

def countdown(seconds: int):
    print("Countdown started!")
    print("-" * 20)

    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        print(f"  Time left: {minutes:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("  Time left: 00:00     ")
    print("-" * 20)
    print("Time is up!")

# Test
seconds = int(input("Enter seconds: "))
countdown(seconds)