class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.starting_num = 0
        self.result_numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.starting_num < self.step*self.count:
            temp = self.starting_num
            self.starting_num += self.step
            return temp
        else:
            raise StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)