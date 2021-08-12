class HashTable:
    def __init__(self):
        self.max_length = 4
        self.__keys = [None] * self.max_length
        self.__values = [None] * self.max_length

    def __setitem__(self, key, value):
        index = self.get_available_index(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key is not in dict")

    def get_available_index(self, key):
        index = self.hash(key)
        return self.check_if_available(index)

    def hash(self, key):
        index = sum(ord(x) for x in key) % self.max_length
        return index

    def check_if_available(self, index):
        if self.__keys[index] is None:
            return index
        return self.check_if_available(index + 1)

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __len__(self):
        return len([x for x in self.__keys if x is not None])

    def capacity(self):
        return self.max_length

    def keys(self):
        return [x for x in self.__keys if x is not None]

    def values(self):
        keys = self.keys()
        valid_values = []
        for key in keys:
            index = self.__keys.index(key)
            valid_values.append(self.__values[index])
        return valid_values

    def __resize(self):
        self.__keys.extend([None] * self.max_length)
        self.__values.extend([None] * self.max_length)
        self.max_length *= 2

    def __repr__(self):
        result = []
        for key in self.keys():
            result.append(f"{key}: {self.get(key)}")
        return "{" + ", ".join(result) + "}"

table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print(table)