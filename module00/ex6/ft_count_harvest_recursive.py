def ft_count_harvest_recursive():
	print("Days until harvest: ")
	total = int(input())
	count_days(total)
	print("Harvest time!")

def	count_days(total):
	n = 1
	while n != total:
		print(f"Day {n}")
		n += 1
	print(f"Day {n}")