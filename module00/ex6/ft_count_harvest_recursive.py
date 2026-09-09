def ft_count_harvest_recursive():
    print("Days until harvest: ")
    total = int(input())
    day = 1
    count_days(day, total)
    print("Harvest time!")


def count_days(day, total):
    if (day > total):
        return
    print(f"Day {day}")
    day = day + 1
    count_days(day, total)
