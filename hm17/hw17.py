numbers = []

while True:
    user_input = input("X=? ")

    try:
        val = int(user_input)
    except ValueError:
        continue

    if val == -1:
        break

    if val > 0:
        numbers.append(val)

total_count = len(numbers)

if total_count > 0:
    average = sum(numbers) / total_count
    print(f"The entered values are {numbers}.")
    print(f"Total: {total_count} natural numbers entered.")
    print(f"Average: {average:.1f}")
else:
    print("No natural numbers were entered.")