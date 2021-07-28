def fibonacci():
    f1 = 0
    f2 = 1
    yield f1
    yield f2
    while True:
        current_num = f1 + f2
        yield current_num
        f1 = f2
        f2 = current_num

generator = fibonacci()
for i in range(5):
    print(next(generator))