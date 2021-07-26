def genrange(start, end):
    while not start > end:
        yield start
        start += 1

print(list(genrange(1, 10)))