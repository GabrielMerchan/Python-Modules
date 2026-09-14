def recursion(start, end):
    if start > end:
        return 1
    print("Day", start)
    recursion(start + 1, end)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    i = 1
    recursion(i, days)
