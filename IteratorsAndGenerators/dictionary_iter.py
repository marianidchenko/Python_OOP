class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.next_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_index < len(self.dictionary):
            current_index = self.next_index
            self.next_index += 1
            return self.dictionary[current_index]
        else:
            raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)