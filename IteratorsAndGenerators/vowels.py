class vowels:
    def __init__(self, string):
        self.string = string
        self.vowel_keys = "AEIOUYaeiouy"
        self.vowels_from_string = [x for x in self.string if x in self.vowel_keys]
        self.current = 0
        self.end = len(self.vowels_from_string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration()
        else:
            index = self.current
            self.current += 1
            return self.vowels_from_string[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)