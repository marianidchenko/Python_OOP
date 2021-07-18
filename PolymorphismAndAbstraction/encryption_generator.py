class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        result = ''
        for char in self.text:
            char = ord(char) + other
            if char > 126:
                difference = char - 126
                char = 31 + difference
            elif char < 32:
                difference = 32 - char
                char = 127 - difference
            char = chr(char)
            result += char
        return result


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))