def average(nums):
    return sum(nums) / len(nums)


def median(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def main():
    with open("numbers1.txt") as f:
        text = f.readline().strip()

    nums = [int(x) for x in text.split()]

    print(f"총 숫자의 개수: {len(nums)}")
    print(f"평균: {average(nums):.1f}")
    print(f"최댓값: {max(nums)}")
    print(f"최솟값: {min(nums)}")
    print(f"중앙값: {median(nums)}")


if _name_ == "_main_":
    main()