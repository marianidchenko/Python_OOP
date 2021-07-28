class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_index = 0
        self.length = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.number:
            index = self.current_index
            self.current_index += 1
            return self.sequence[index % self.length]
        else:
            raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')