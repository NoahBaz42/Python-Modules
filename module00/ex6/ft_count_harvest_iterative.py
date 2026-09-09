def ft_count_harvest_iterative():
    print("Days until harvest: ")
    days = int(input())
    daycount = 1
    while daycount != days:
        print(f"Day {daycount}")
        daycount += 1
    print(f"Day {daycount}")
    print("Harvest time!")
