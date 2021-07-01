n = int(input())


def print_row(size, star_count):
    for row in range(size-star_count):
        print(" ", end='')
    for row in range(1, star_count):
        print("*", end=' ')
    print("*")


for amount_of_stars in range(1, n):
    print_row(n, amount_of_stars)

for amount_of_stars in range(n, 0, -1):
    print_row(n, amount_of_stars)